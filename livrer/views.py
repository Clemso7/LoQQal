# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from delivery.forms import DemandForm
from delivery.models import Demand, Author
from django.http import HttpResponseRedirect
from address.forms import AddressField
from address.models import AddressField
from django.db.models import Count
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from delivery.models import Author
from django.contrib.auth.decorators import login_required
from django.db.models import FilteredRelation, Q
from django.utils.translation import ugettext_lazy as _



# index view
def home (request):
    livraison=Demand.objects.all().count()
    livraison_T=livraison + 48
    km=livraison * 5
    km_T=km + 240
    CO2 = km_T * 206
    context = {
        'livraison_T':livraison_T,
        'km_T':km_T,
        'CO2': CO2

    }
    return render(request, 'livrer/index.html', locals()) 


# about view
def about(request):
    return render(request, 'livrer/about.html', locals())

# Faq view
def faq(request):
    return render(request, 'livrer/faq.html', locals())

# Terms of service view
def privacy_policy(request):
    return render(request, 'livrer/privacy-policy.html', locals())

# Contact view
def contact(request):
    return render(request, 'livrer/contact.html', locals())


# Ads search/filter view
def ads_search(request):
    auts = Author.objects.filter(user_type="Compagny")
    search_ads = request.GET.get('search')
    erreur =_(" Please, enter your package id")
    erreur2 =_(" Sorry, your id is not a number")
   
    try:
        
        search_ads = int(search_ads)
    
        
        if search_ads :
            
            ads = Demand.objects.filter(pk=search_ads)
            
            context ={'aut': auts, 'ads': ads}
            return render(request, 'livrer/ads-search.html', context)

        else: 
        # If not searched, return default posts
            messages.error(request, erreur)
            return render(request, 'livrer/index.html')
             

    except:
        messages.error(request, erreur2)
        return render(request, 'livrer/index.html')
       