from django.urls import path
from . import views

app_name = 'file_upload'

urlpatterns = [
    path('<int:the_id>', views.uploadAlbum, name="uploadAlbum"),
    path('<int:album_id>/uploadSong', views.uploadSong, name="uploadSong")
]