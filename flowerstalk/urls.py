from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'flowerstalk'

urlpatterns = [
    path('', views.index_page, name="index_page"),
    path('about/', views.about_page, name="about_page"),
    path('contact-us/', views.contact_page, name="contact_page"),
    path('flowers/', views.flowers_list, name="flowers_list"),
    path('gifts/', views.gifts_list, name="gifts_list"),
    path('shop/<slug>/', views.item_detail, name="item_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
