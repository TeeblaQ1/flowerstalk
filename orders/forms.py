from django import forms
from django.forms import fields
from .models import Order, PaymentUpload

class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'lga', 'options', 'personalized_note', 'total_price']

class PaymentUploadForm(forms.ModelForm):

    class Meta:
        model = PaymentUpload
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PaymentUploadForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
