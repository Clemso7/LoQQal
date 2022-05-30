from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve 
from django.utils.translation import ugettext_lazy as _



urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('ads-search/', views.ads_search, name='ads-search'),
]