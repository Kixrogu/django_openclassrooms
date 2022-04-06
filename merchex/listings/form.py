from dataclasses import fields
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from random import choices
from tkinter import ACTIVE
from listings.models import models
from listings.models import Band
from listings.models import Artist

class ContactUsForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandAdd(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'

class ArtistAdd(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
    