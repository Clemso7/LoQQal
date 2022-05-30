from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import timedelta
# importing messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import datetime
from django.contrib.auth.forms import User
from delivery.models import Author, Demand
from django.core.paginator import Paginator
from authentication.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


# Model Forms.timedelta(days=365)
# Profile Dashboard view
@login_required(login_url='login')

def profile_dashboard(request):
    dt = datetime.datetime.now()
    wk = dt.isocalendar()[1]

    jan = request.user.author.demand_set.all().filter(published_date__month=1).count()
    fev = request.user.author.demand_set.all().filter(published_date__month=2).count()
    mar = request.user.author.demand_set.all().filter(published_date__month=3).count()
    apr = request.user.author.demand_set.all().filter(published_date__month=4).count()
    may = request.user.author.demand_set.all().filter(published_date__month=5).count()
    jun = request.user.author.demand_set.all().filter(published_date__month=6).count()
    jul = request.user.author.demand_set.all().filter(published_date__month=7).count()
    aug = request.user.author.demand_set.all().filter(published_date__month=8).count()
    sep = request.user.author.demand_set.all().filter(published_date__month=9).count()
    oct = request.user.author.demand_set.all().filter(published_date__month=10).count()
    nov = request.user.author.demand_set.all().filter(published_date__month=11).count()
    dec = request.user.author.demand_set.all().filter(published_date__month=12).count()
    ads_posted = request.user.author.demand_set.all().order_by('-published_date') 
    featured_ads = request.user.author.demand_set.all().filter(published_date__week=wk).count() * 6
    total_ads = request.user.author.demand_set.all().filter(published_date__week=wk).count()
    paginator = Paginator(ads_posted, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jan' : jan,
        'fev' : fev,
        'mar' : mar,
        'apr' : apr,
        'may' : may,
        'jun' : jun,
        'jul' : jul,
        'aug' : aug,
        'sep' : sep,
        'oct' : oct,
        'nov' : nov,
        'dec' : dec,
        'ads_posted' : ads_posted,
        'total_ads' : total_ads,
        'featured_ads' : featured_ads,
        'page_obj': page_obj
    }
    
    return render(request, 'profiles/account-dashboard.html', context)

# Profile Settings view
@login_required(login_url='login')
def profile_settings(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.author)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your profile has been updated successfully!")
            return redirect('profile-settings')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.author)

    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request, 'profiles/account-setting.html', context)

# Profile view
@login_required(login_url='login')
def profile_ads(request):
    return render(request, 'profiles/all-ads.html')

# Profile Favorite  view
@login_required(login_url='login')
def profile_favorite_ads(request):
    return render(request, 'profiles/favourite-ads.html')

# Profile Delete view
@login_required(login_url='login')
def profile_close(request):
    return render(request, 'profiles/account-close.html')

# facture view
def facture(request):
    dt = datetime.datetime.now()
    wk = dt.isocalendar()[1]
    ads_posted = request.user.author.demand_set.all().order_by('-published_date') 
    featured_ads = request.user.author.demand_set.all().filter(published_date__week=wk).count() * 6
    total_ads = request.user.author.demand_set.all().filter(published_date__week=wk).count()
    context = {
        
        'ads_posted' : ads_posted,
        'total_ads' : total_ads,
        'featured_ads' : featured_ads,
        
    }
    
    return render(request, 'profiles/invoice-detail.html', context)