from io import BytesIO
from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, PaymentUpload
import time
import os

# os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
# GTK_FOLDER = r'C:\Program Files\GTK3-Runtime Win64\bin'
# os.environ['PATH'] = GTK_FOLDER + os.pathsep + os.environ.get('PATH', '')
from weasyprint import HTML, CSS


# current_url = 'http://127.0.0.1:8000'
current_url = 'https://flowerstalkng.herokuapp.com'

@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
    f'You have successfully placed an order.' \
    f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'ikoyiflowerstalk@gmail.com', [order.email])
    # print(mail_sent)
    return mail_sent


def order_created_mail(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    time.sleep(5)
    order = Order.objects.get(id=order_id)
    order_id = 'FLWSTK'+ str(order.id).zfill(5)
    current_site_url = f'{current_url}/orders/create/?orderId={order_id}'
    subject = f'Order {order_id} has been created'
    message = f'Dear {order.name},\n\n' \
    f'You have successfully placed an order. ' \
    f'Your order ID is {order_id}. \n\n' \
    f'Please use the link below if you would like to upload your proof of payment at a later time: \n' \
    f'{current_site_url} \n' \
    f'Best Regards.\nFlowerstalk Nigeria. \n\n\n\n' \
    f'Feel free to contact us \n' \
    f'Tel - 09051613991 \n' \
    f'Email - ikoyiflowerstalk@gmail.com \n' \
    f'Address - 2, Oyinkan Abayomi Drive, Ikoyi, Lagos.' 
    html_message = render_to_string('orders/order/mail_template.html', {'order': order, 'order_id': order_id, 'current_site_url': current_site_url})
    email = EmailMessage(subject, html_message, 'ikoyiflowerstalk@gmail.com', [order.email])
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'order_{order_id}_pending.pdf', out.getvalue(), 'application/pdf')
    email.content_subtype = 'html'
    email.send()


def order_created_mail_admin(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    time.sleep(10)
    order_admin = Order.objects.get(id=order_id)
    order_id_admin = 'FLWSTK'+ str(order_admin.id).zfill(5)
    current_site_url_admin = f'{current_url}/admin/orders/order/{order_admin.id}'
    subject_admin = f'New Order Alert'
    message_admin = f'''
        A new order has just been placed on Flowerstalk \n\n
        Order ID: \t\t{order_id_admin}
        Customer Name: \t\t{order_admin.name}
        Customer Phone Number: \t{order_admin.phone}
        Customer Email Address: \t{order_admin.email}
        Order Amount: \t\t{order_admin.total_price}
        Order Option: \t\t{order_admin.options} \n\n
        Please use the link below to view the order details on the admin page:
        {current_site_url_admin} \n\n\n\n
        Feel free to contact us
        Tel - 09051613991
        Email - ikoyiflowerstalk@gmail.com
        Address - 2, Oyinkan Abayomi Drive, Ikoyi, Lagos.
    '''
    mail_sent = send_mail(subject_admin, message_admin, 'ikoyiflowerstalk@gmail.com', ['ikoyiflowerstalk@gmail.com'])
    # print('Admin: ', mail_sent)
    return mail_sent


def payment_created_mail_admin(payment_id):
    """
    Task to send an e-mail notification when a payment is
    successfully created.
    """
    time.sleep(10)
    payment_admin = PaymentUpload.objects.get(id=payment_id)
    order_id_admin = 'FLWSTK'+ str(payment_admin.orderItem.id).zfill(5)
    current_site_url_admin = f'{current_url}/admin/orders/paymentupload/{payment_admin.id}/change/'
    subject_admin = f'New Payment Uploaded!'
    message_admin = f'''
        A new proof of payment has just been uploaded to Flowerstalk \n\n
        Order ID: \t\t{order_id_admin}
        Customer Name: \t\t{payment_admin.orderItem.name}
        Customer Phone Number: \t{payment_admin.orderItem.phone}
        Customer Email Address: \t{payment_admin.orderItem.email}
        Payment Amount: \t\t{payment_admin.amount_paid}
        Order Option: \t\t{payment_admin.orderItem.options} \n\n
        Please use the link below to view the order details on the admin page:
        {current_site_url_admin} \n\n\n\n
        Feel free to contact us
        Tel - 09051613991
        Email - ikoyiflowerstalk@gmail.com
        Address - 2, Oyinkan Abayomi Drive, Ikoyi, Lagos.
    '''
    mail_sent = send_mail(subject_admin, message_admin, 'ikoyiflowerstalk@gmail.com', ['ikoyiflowerstalk@gmail.com'])
    # print('Admin Payment: ', mail_sent)
    return mail_sent


def payment_confirmed_mail_admin(order_id):
    """
    Task to send an e-mail notification when a payment has been confirmed.
    """
    time.sleep(10)
    order_payment = Order.objects.get(id=order_id)
    order_payment_id = 'FLWSTK'+ str(order_payment.id).zfill(5)
    subject = f'Payment Confirmed! [Order {order_id}]'
    message = f'Dear {order_payment.name},\n\n' \
    f'Your payment has been confirmed, thank you for shopping with us. \n' \
    f'Our team is processing your order. Your order ID is {order_payment_id}.\n' \
    f'If there will be need, one of our representative will contact you. \n' \
    f'Please find attached your receipt. \n' \
    f'Best Regards.\nFlowerstalk Nigeria. \n\n\n\n' \
    f'Feel free to contact us \n' \
    f'Tel - 09051613991 \n' \
    f'Email - ikoyiflowerstalk@gmail.com \n' \
    f'Address - 2, Oyinkan Abayomi Drive, Ikoyi, Lagos.' 
    html_message = render_to_string('orders/order/mail_template_payment.html', {'order': order_payment, 'order_id': order_payment_id})
    email = EmailMessage(subject, html_message, 'ikoyiflowerstalk@gmail.com', [order_payment.email])
    html = render_to_string('orders/order/pdf.html', {'order': order_payment})
    out = BytesIO()
    stylesheets=[CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'order_{order_payment_id}.pdf', out.getvalue(), 'application/pdf')
    email.content_subtype = 'html'
    email.send()
