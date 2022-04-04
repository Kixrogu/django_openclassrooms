from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Artist

def hello(request):
    bands = Band.objects.all()
    artists = Artist.objects.all()
    return render(request, 
        'listings/hello.html',
        {'bands': bands,
        'artists': artists}
    )


def aboutus(request):
    return HttpResponse('<h1>A propos de nous</h1><p1>Franchement ça marche bien</p1>')

def listings(request):
    return HttpResponse('<h1>Ceci est une liste</h1>')

def contactus(request):
    return HttpResponse('<p1>Mail : maxime.pile@alur3.com</p1><p1>Tel : +33 29 82 54 23</p1>')