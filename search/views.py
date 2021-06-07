from django.shortcuts import render
from django.db.models import Q
from homepage.models import Album

def lookUp(request):

    return render(request, 'search/my_search.html')

def results(request):

    my_search = request.GET['search']

    albums = Album.objects.filter(
        Q(album_title__icontains=my_search)
    )

    context = {
        'album':albums,
        'my_search':my_search,
    }

    return render(request, 'search/results.html', context)
