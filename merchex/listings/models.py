from msvcrt import open_osfhandle
from pyexpat import model
from random import choices
from tkinter import ACTIVE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import admin


class Band(models.Model):
    name = models.fields.CharField(max_length=100)

    class Genre(models.TextChoices):
        RAP = 'RAP'
        POP = 'POP'
        DISCO = 'DC'
        ELECTRO = 'ELEC'
        NON_DEFINI = 'ND'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)


    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    #Sert à afficher directement le nom sur le site admin CRUB
    #def __str__(self):
     #   return f'{self.name}, {self.genre}, {self.pk}'

    def __str__(self):
        return f'{self.name}'

class Artist(models.Model):
    name = models.fields.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class Listings(models.Model):
    name = models.fields.CharField(max_length=50)
    description = models.fields.CharField(max_length=150)
    sold = models.fields.BooleanField(default=0)
    
    class Type(models.TextChoices):
        RECORDS = 'RC'
        CLOTHING = 'CLOTH'
        POSTERS = 'POST'
        MISCELLANEOUS = 'MISC'
    
    type = models.fields.CharField(choices=Type.choices, max_length=10)

    band = models.ForeignKey(Band, null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.SET_NULL)
