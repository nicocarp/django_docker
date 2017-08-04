# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from django.core.mail import send_mail

@shared_task
def add(x, y):
    print "sumando", x, y
    time.sleep( 5 )
    resultado = x + y
    print "fin sumando por mandar MAIL"
    send_mail(subject='Desde django', 
              message='Hay que aprobar seguridad..', 
              from_email='calfuquir.nico2@gmail.com',
              recipient_list=['ccsjgs1990@gmail.com'], 
              fail_silently=False)
    return resultado

