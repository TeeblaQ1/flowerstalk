import threading
from django.shortcuts import render

from cart.forms import CartAddProductForm
from .models import OrderItem, Order
from .forms import OrderCreateForm, PaymentUploadForm
from cart.cart import Cart
from .tasks import order_created, order_created_mail, order_created_mail_admin, payment_created_mail_admin

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
