from django.db import models
from django.contrib.auth.models import User, auth


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob =   models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15, unique=True)
    adress = models.CharField(max_length=200)
    pro_pic = models.ImageField(upload_to='pics')
    last_edit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
    
    class Meta:
        ordering = ['phone_number']

class FavouriteSong(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    song_id = models.IntegerField()
    song_name = models.CharField(max_length=200)
    date_favourited  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_name


class Album(models.Model):
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=200)
    album_logo = models.ImageField(upload_to='logos')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title  = models.CharField(max_length=200)
    audio = models.FileField(upload_to='songs')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_title

class Menu(models.Model):
    link_name = models.CharField(max_length=200)
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.link_name

    