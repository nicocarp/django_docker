# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from django.core.mail import send_mail

@shared_task
def enviar_mail():
    time.sleep( 5 )

    mge = "Un mensaje desde django"
    send_mail(subject='Desde django', 
              message=mge, 
              from_email='calfuquir.nico2@gmail.com',
              recipient_list=['norfuen@hotmail.com'], 
              fail_silently=False)
    return 1
