from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import tasks
import random
def get_order(get):
    if "o" in get:
        return get["o"]


@login_required(login_url='login')
def inicio(request):
    return render(request, "inicio/inicio.html")


def paginaEnConstruccion(request):
    return render(request, "paginaEnConstruccion.html")

def test_con_celery(request):
    x = random.choice([1,2,3])
    y = random.choice([1,2,3])
    res = tasks.add.delay(x,y)
    return render(request, "test_celery.html", {'resultado':1})

def test_sin_celery(request):
    x = random.choice([1,2,3])
    y = random.choice([1,2,3])
    res = tasks.add(x,y)
    return render(request, "test_celery.html", {'resultado':res})