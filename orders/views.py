import threading
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.conf import settings

from cart.forms import CartAddProductForm
from .models import OrderItem, Order
from .forms import OrderCreateForm, PaymentUploadForm
from cart.cart import Cart
from .tasks import order_created, order_created_mail, order_created_mail_admin, payment_created_mail_admin, payment_confirmed_mail_admin
import os

os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
from weasyprint import HTML, CSS

# Create your views here.
def order_create(request):
    cart = Cart(request)
    vat = 0
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order_id = 'FLWSTK'+ str(order.id).zfill(5)
            order_price = order.total_price
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            
            cart.clear()
            # order_created.delay(order.id)
            threadObj = threading.Thread(target=order_created_mail, args=[order.id])
            threadObj.start()
            threadObjAdmin = threading.Thread(target=order_created_mail_admin, args=[order.id])
            threadObjAdmin.start()
            return render(request, 'orders/payment/proof_upload.html', {'order': order, 'order_id': order_id, 'order_price': order_price})
    
    elif request.GET.get('orderId'):
        custom_order_id = str(request.GET.get('orderId'))
        order_id = int(custom_order_id[6:])
        order = Order.objects.get(id=order_id)
        return render(request, 'orders/payment/proof_upload.html', {'order_id': custom_order_id, 'order_price': order.total_price})

    else:
        form = OrderCreateForm()
        total_price = 0
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
            item_price = item['quantity'] * int(item['price'])
            total_price += item_price
        vat = 0.075 * total_price
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form, 'vat': vat})

def proof_upload(request):
    if request.method == 'POST':
        form = PaymentUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            payment = form.save()
            threadObjAdmin = threading.Thread(target=payment_created_mail_admin, args=[payment.id])
            threadObjAdmin.start()
            return render(request, 'orders/payment/proof_upload.html', {'form': form, 'success': True})
    else:
        form = PaymentUploadForm()
        return render(request, 'orders/payment/proof_upload.html', {'form': form})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})


@staff_member_required
def admin_confirm_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if not order.paid:
        order.paid = True
        order.save()
        # Send email to customer
        threadObj = threading.Thread(target=payment_confirmed_mail_admin, args=[order.id])
        threadObj.start()
    return redirect('admin:orders_order_change', order.id)

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    HTML(string=html).write_pdf(response, stylesheets=[CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response
