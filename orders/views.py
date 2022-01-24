from django.shortcuts import render

from cart.forms import CartAddProductForm
from .models import OrderItem
from .forms import OrderCreateForm, PaymentUploadForm
from cart.cart import Cart

# Create your views here.
def order_create(request):
    cart = Cart(request)
    vat = 0
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order_id = 'FLWSTK'+ str(order.id).zfill(5)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            
            cart.clear()
            return render(request, 'orders/payment/proof_upload.html', {'order': order, 'order_id': order_id})
    
    elif request.GET.get('orderId'):
        order_id = str(request.GET.get('orderId'))
        return render(request, 'orders/payment/proof_upload.html', {'order_id': order_id})

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
            form.save()
            return render(request, 'orders/payment/proof_upload.html', {'form': form, 'success': True})
    else:
        form = PaymentUploadForm()
        return render(request, 'orders/payment/proof_upload.html', {'form': form})