# -*- coding: utf-8 -*-
from django.contrib import admin
from delivery.models import Author, Demand, Driver, Mandat
from django.utils.html import format_html




class DemandAdmin(admin.ModelAdmin):
    
    # def thumbnail(self, object):
    #     return format_html('<img src="{}" width="40">'.format(object.image.url))
    
    # Display columns in horizontal list
    list_display = ('id', 'service', 'author', 'name', 'phone', 'autocomplete', 'description', 'email','published_date','is_active',)
    
    # Columns having links
    list_display_links = ('id', 'author')

    # Editable columns
    list_editable = ('is_active',) 

    # Filterable columns
    list_filter = ('author','published_date')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',  'user_type', 'business_name', 'business_phone', 'business_address')
    list_editable = ('user_type',)
    list_filter = ('user_type',)
    

class DriverAdmin(admin.ModelAdmin):
    list_display = ('deliver', 'phone', 'address')

class MandatAdmin(admin.ModelAdmin):
    list_display = ('colis', 'statut', 'date')
    list_editable = ('statut',)
   
class AdsImagesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Demand, DemandAdmin)

admin.site.register(Author, AuthorAdmin)

admin.site.register(Driver, DriverAdmin)

admin.site.register(Mandat, MandatAdmin)