from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('payment-proof/', views.proof_upload, name='payment_proof'),
    path('admin/order/<int:order_id>/', views.admin_order_detail, name="admin_order_detail"),
    path('admin/order/<int:order_id>/confirm_payment/', views.admin_confirm_payment, name="admin_confirm_payment"),
    path('admin/order/<int:order_id>/pdf/', views.admin_order_pdf, name="admin_order_pdf"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
