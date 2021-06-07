from django.shortcuts import render, redirect
from homepage.models import Album, Song
from django.contrib.auth.models import User

def uploadAlbum(request, the_id):

    if request.method == 'POST':
        title = request.POST['album_title']
        logo = request.FILES['image']
        user = User.objects.get(pk=the_id)
        album = Album()
        album.artist=user
        album.album_title=title
        album.album_logo=logo
        album.save()
        return redirect('/')

    else:
        return render(request, 'file_upload/album_upload.html')

def uploadSong(request, album_id):

    if request.method == 'POST':
        songtitle = request.POST['song_title']
        audio = request.FILES['audio']
        album = Album.objects.get(pk=album_id)
        song = Song()
        song.album = album
        song.song_title=songtitle
        song.audio=audio
        song.save()
        return redirect('/album_details/' + str(album_id))
    else:
        album = Album.objects.get(pk=album_id)
        return render(request, 'file_upload/song_upload.html', {'album':album})
