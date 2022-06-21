from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from . import models

def index(request):
    return HttpResponse("Welcome")


def all_windows(request):
    windows = models.Window.objects.all()
    context = {
        'windows': windows,
    }
    return render(request, 'all_windows.html', {'context': context})


def window_detail(request, window_id):
    window = get_object_or_404(models.Window, id=window_id)
    context = {
        'window': window,
    }
    return render(request, 'window.html', {'context': context})

def all_glasses(request):
    glass = models.Glass.objects.all()
    context = {
        'glass': glass,
    }
    return render(request, 'glass.html', {'context': context})