from django.contrib import admin

from listings.models import Band
from listings.models import Listings
from listings.models import Artist


admin.site.register(Artist)

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active')

class ListingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'band', 'sold')




admin.site.register(Band, BandAdmin)
admin.site.register(Listings, ListingsAdmin)