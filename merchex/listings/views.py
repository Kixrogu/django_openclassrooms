from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings.models import Band
from listings.models import Artist
from listings.models import Listings
from listings.form import ContactUsForm
from django.core.mail import send_mail


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



def contactus(request):
    #print('La méthode de requête est : ', request.method)
    #print('Les données de la requête sont : ', request.POST)

    if request.method == 'POST':
        form = ContactUsForm(request.POST)


        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["name"] or "anonyme"} via Merchex - Contact us',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')


    else:
        form = ContactUsForm() 

    return render(request,
        'listings/contactus.html',
        {'form': form})


def email_sent(request):
    return render(request, 'listings/email-sent.html')