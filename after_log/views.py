from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Album, Menu
from django.contrib.auth.models import User

def logged_in(request):


    return render(request, "after_log/after_log.html")
