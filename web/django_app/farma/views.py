from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import tasks
import random
from medicamentos import models as medicamento_models
from django.core import serializers
from easy_pdf.views import PDFTemplateView

def get_order(get):
    if "o" in get:
        return get["o"]

@login_required(login_url='login')
def inicio(request):
    return render(request, "inicio/inicio.html")

def paginaEnConstruccion(request):
    return render(request, "paginaEnConstruccion.html")

def test_con_celery(request):
    data = serializers.serialize("json", medicamento_models.Monodroga.objects.all())
    tasks.enviar_mail.delay()
    #x = random.choice([1,2,3])
    #y = random.choice([1,2,3])
    #res = tasks.add.delay(x,y)
    return render(request, "test_celery.html", { "monodrogas": data})

def test_sin_celery(request):
    data = serializers.serialize("json", medicamento_models.Monodroga.objects.all())
    #x = random.choice([1,2,3])
    #y = random.choice([1,2,3])
    #res = tasks.add(x,y)
    tasks.enviar_mail()
    return render(request, "test_celery.html", {'monodrogas':data})