from django.urls import path

from .import views

urlpatterns = [
    path('dashboard/', views.profile_dashboard, name='dashboard'),
    path('profile-settings/', views.profile_settings, name='profile-settings'),
    path('my-ads/', views.profile_ads, name='profile-ads'),
    path('profile-close/', views.profile_close, name='profile-close'),
    path('invoice-detail/', views.facture, name='invoice-detail'),
    
]