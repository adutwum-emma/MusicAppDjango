from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('lookUp', views.lookUp, name="lookUp"),
    path('results', views.results, name='results')
]