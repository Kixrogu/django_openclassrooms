from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Artist
from listings.models import Listings

def listings(request):
    listings = Listings.objects.all()
    return render(request, 
        'listings/listings.html',
        {'listings': listings}
    )

def band_list(request):
    bands = Band.objects.all()
    return render(request,
        'listings/band_list.html', 
        {'bands': bands}
    )

def artist_list(request):
    artists = Artist.objects.all()
    return render(request,
        'listings/artist_list.html', 
        {'artists': artists}
    )


def band_info(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,'listings/band_info.html', 
        {'band': band}
    )

def artist_info(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    return render(request, 'listings/artist_info.html',
        {'artist': artist}
    )


def aboutus(request):
    return HttpResponse('<h1>A propos de nous</h1><p1>Franchement ça marche bien</p1>')

def contactus(request):
    return HttpResponse('<p1>Mail : maxime.pile@alur3.com</p1><p1>Tel : +33 29 82 54 23</p1>')