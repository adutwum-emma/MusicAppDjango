from django.shortcuts import render, redirect, get_object_or_404
from homepage.models import Album, Song, Menu, FavouriteSong
from django.contrib import messages


def details(request, album_id):
    
    album = Album.objects.get(pk=album_id)

    context = {
        'album':album,
    }
    return render(request, 'album_details/details.html', context)

def delete(request):

    my_song_id = request.POST['song_id']

    try:
        song = Song.objects.get(pk=request.POST['song'])
    
    except (KeyError, Song.DoesNotExist):
        messages.info(request, "You did not select any song")
        return redirect('/album_details' + '/' + str(my_song_id))
    else:
        song.delete()
        return redirect('/album_details' + '/' + str(my_song_id))
