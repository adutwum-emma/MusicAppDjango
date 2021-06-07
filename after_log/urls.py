from django.urls import path
from . import views

app_name = 'after_log'

urlpatterns = [
    path('logged_in/', views.logged_in, name="views.logged_in"),
]