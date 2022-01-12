from django.db import models
from flowerstalk.models import Product

# Create your models here.
class Order(models.Model):
    ORDER_OPTIONS = (
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup')
    )

    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    options = models.CharField(max_length=10, choices=ORDER_OPTIONS, default='delivery')
    lga = models.CharField(max_length=128, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    personalized_note = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.id} - {self.name}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity


class PaymentUpload(models.Model):
    orderItem = models.ForeignKey(Order, related_name='order_payment', on_delete=models.CASCADE)
    payment_date = models.DateField(verbose_name='Date of Payment')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/%Y/%m/', null=True, blank=True)


    def __str__(self):
        return str(self.id)

