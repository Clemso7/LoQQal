from django.urls import path

from .import views

urlpatterns = [
    path('post-ads/', views.post_ads, name='post-ads'),
    path('post-demands/', views.post_demands, name='post-demands')   
]