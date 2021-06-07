from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Menu
from django.contrib.auth.models import User

def index(request):

    album = Album.objects.all()
    menu = Menu.objects.all()[:5]

    context = {
        'album': album,
        'menu': menu,
    }

    return render(request, 'homepage/body.html', context)
