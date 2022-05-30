from django.forms import ModelForm
# importing default user registration form
from django.contrib.auth.forms import UserCreationForm
# importing built-in user model
from django.contrib.auth.forms import User
from django import forms
from delivery.models import Author
from phone_field import PhoneField
from address.models import AddressField
from address.forms import AddressField
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext_lazy as _



class UserRegistrationForm(UserCreationForm):
    # Styling the username form fields
    util = _('Username')
    username = forms.CharField( widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'username', 
        'placeholder': util
    }))
    mdp = _('Password')
    # Styling the password1 form fields
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',  
        'name': 'password1', 
        'placeholder': mdp
    }))

    # Styling the password2 form fields
    mdp2 = _("Confirm password")
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',  
        'name': 'password2', 
        'placeholder': mdp2
    }))
    
    # Making the email field required 
    email = forms.EmailField(required=True)

    # Styling the email form fields
    cour = _('Email Address')
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',  
        'placeholder': cour
    }))

    
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    def clean_email(self):
        output = _("This Email address is already in use.")
        email = self.cleaned_data['email']
        duplicate_email = User.objects.filter(email=email).exists()
        print("Email Taken")
        if duplicate_email:
            raise forms.ValidationError(output)
        return email


class EmailValidationOnForgotPassword(PasswordResetForm):
    cour = _('Email Address')
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',  
        'placeholder': cour
    }))

    def clean_email(self):
        output = _("There is no user registered with the specified email address!")
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError(output)

        return email

class EmailSetPassword(SetPasswordForm):
    # Styling the password1 form fields
    mdp = _('Password')
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',  
        'name': 'new_password1', 
        'placeholder': mdp
    }))

    # Styling the password2 form fields
    mdp2 = _("Confirm password")
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',  
        'name': 'new_password2', 
        'placeholder': mdp2
    }))

# Updating the User registration form
class UserUpdateForm(ModelForm):
    prenom = _('First Name')
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'first_name', 
        'placeholder': prenom
    }))

    nom = _('Last Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'last_name', 
        'placeholder': nom
    }))

    cour = _('Email Address')
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',  
        'placeholder': cour
    }))  

    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        # exclude = ['user']

    
USER_CHOICES =(
        ("Individual","Individual"),
        ("Compagny","Compagny")
    )   
# Updating the profile form
class ProfileUpdateForm(ModelForm):
    serv = _('individual or compagny')
    user_type = forms.ChoiceField(choices=USER_CHOICES, widget=forms.Select(attrs={
        'placeholder': 'Service type',
        'class': 'form-control',
        'name': 'service',
        'placeholder': serv
    }))

    busi = _( 'Business name or username')
    business_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'business_name', 
        'placeholder': busi
    }))

    tel = _('Business or personal phone')
    business_phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'business_phone', 
        'placeholder': tel
    }))

    adr = _('Business or home address')
    business_address = AddressField(widget=forms.TextInput(attrs={
        'type': 'text',
        'id':'autocomplete',
        'class': 'form-control',  
        'name': 'autocomplete', 
        'placeholder': adr
        
    }))
    class Meta:
        model = Author
        fields = ['user_type','business_name', 'business_address','business_phone', 'profile_pic']
    