from django.db import models
from django.urls.base import reverse

# Create your models here.
class FlowerManager(models.Manager):
    def get_queryset(self):
        return super(FlowerManager, self).get_queryset().filter(category='flowers')

class GiftManager(models.Manager):
    def get_queryset(self):
        return super(GiftManager, self).get_queryset().filter(category='gifts')

class Product(models.Model):
    CATEGORY_OPTIONS = (
        ('flowers', 'Flowers'),
        ('gifts', 'Gifts')
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique_for_date='created')
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY_OPTIONS, default='flowers')
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    flowers = FlowerManager()
    gifts = GiftManager()

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('flowerstalk:item_detail', args=[self.slug,])


class ContactUs(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=32)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name
