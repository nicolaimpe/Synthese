from django.shortcuts import render
from django.shortcuts import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import Album, Artist, Track
from .forms import SearchForm


# Create your views here.

def list_albums(request):
    """ Afficher tous les albums de notre liste """
     # Nous sélectionnons tous nos albums

    if request.method == 'POST':
        form = SearchForm(request.POST or None)
        string = form.cleaned_data['string']
        albums = Album.objects.filter(title__unaccent__icontains=string)
        envoi = True
        print("cacca")
        return render(request, 'disks/album_list.html', {'albums': albums})
    else:
        albums = Album.objects.all

        return render(request, 'disks/album_list.html', {'albums': albums})


def view_album(request, id):
    album = get_object_or_404(Album, id=id)
    songs = Track.objects.filter(album_id = id)
    return render(request, 'disks/show_tracks.html', {'songs': songs, 'album': album})

