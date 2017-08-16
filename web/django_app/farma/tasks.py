# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from django.core.mail import send_mail

@shared_task
def add(x, y):
    time.sleep( 5 )
    resultado = x + y
    print "fin sumando por mandar MAIL"
    mge = "%d + %d = %d "%(x,y,resultado)
    send_mail(subject='Desde django', 
              message=mge, 
              from_email='calfuquir.nico2@gmail.com',
              recipient_list=['norfuen@hotmail.com'], 
              fail_silently=False)
    return resultado

