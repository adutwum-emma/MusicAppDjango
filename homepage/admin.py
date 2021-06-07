from django.contrib import admin
from .models import Profile, Album, Song, FavouriteSong, Menu

admin.site.register(Profile)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(FavouriteSong)
admin.site.register(Menu)
