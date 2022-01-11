from django.shortcuts import get_object_or_404, render

from .models import Product
from .forms import ContactUsForm
from cart.forms import CartAddProductForm

# Create your views here.
def flowers_list(request):
    items = Product.flowers.all()
    return render(request, 'flowerstalk/item/list.html', {'items': items, 'category_name': 'Flowers'})

def gifts_list(request):
    items = Product.gifts.all()
    return render(request, 'flowerstalk/item/list.html', {'items': items, 'category_name': 'Gifts'})

def item_detail(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'flowerstalk/item/detail.html', {'item': item, 'cart_product_form': cart_product_form})

def index_page(request):
    todays_deal = Product.objects.all()[:3]
    return render(request, 'flowerstalk/item/index.html', {'deals': todays_deal})

def about_page(request):
    return render(request, 'flowerstalk/item/about.html')

def contact_page(request):
    if request.method == 'POST':
        f = ContactUsForm(request.POST)
        if f.is_valid():
            f.save()
            success = "Thank You! Your message has been submitted sucessfully. We'd get back to you shortly."
            return render(request, 'flowerstalk/item/contact.html', {'form': f, 'success': success})
    else:
        f = ContactUsForm()
    return render(request, 'flowerstalk/item/contact.html', {'form': f})