from celery import shared_task
from django.core.mail import send_mail
from .models import Order, PaymentUpload
import time

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
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.name},\n\n' \
    f'You have successfully placed an order.' \
    f'Your order ID is {order.id}. \n\n' \
    f'Please use the link below if you would like to upload your proof of payment at a later time: \n' \
    f'{current_site_url}' 
    mail_sent = send_mail(subject, message, 'ikoyiflowerstalk@gmail.com', [order.email])
    # print(mail_sent)
    return mail_sent


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
        {current_site_url_admin}
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
        {current_site_url_admin}
    '''
    mail_sent = send_mail(subject_admin, message_admin, 'ikoyiflowerstalk@gmail.com', ['ikoyiflowerstalk@gmail.com'])
    # print('Admin Payment: ', mail_sent)
    return mail_sent
