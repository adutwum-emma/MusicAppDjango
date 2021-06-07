from django.urls import path
from . import views

app_name = 'album_details'

urlpatterns = [
    path('<int:album_id>', views.details, name="details"),
    path('delete', views.delete, name="delete"),
]