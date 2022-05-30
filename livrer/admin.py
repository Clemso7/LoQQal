from django.contrib import admin
from livrer.models import Massages
from django.utils.html import format_html

class MassagesAdmin(admin.ModelAdmin):
    list_display = ('objet','name', 'organisation', 'email', 'phone', 'text')
admin.site.register(Massages, MassagesAdmin)