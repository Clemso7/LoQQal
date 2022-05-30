from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import EmailField
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from address.models import AddressField
from django.db import models
from django.forms import ModelForm
from phone_field import PhoneField
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _






class Author(models.Model):
    """ Model for customers """
    USER_CHOICES =(
        ("Individual","Individual"),
        ("Compagny","Compagny")
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_type = models.CharField(verbose_name=_('Person or Compagny'), max_length=10, choices=USER_CHOICES, default='Individual')
    profile_pic = models.ImageField(verbose_name=_('Picture'), upload_to='profile_pics', null=True, blank=True)
    business_name = models.CharField(verbose_name=_('Business name or Username'), max_length=100, null=True, blank=True, help_text=_('Business name or Username') )
    business_phone = PhoneField(verbose_name=_('Business or personal phone'), null=True, blank=True, help_text=_('Business or personal phone'))
    business_address =models.CharField(verbose_name=_('Business or home address'), null=True, blank=True, max_length=300, help_text=_('Business or home address'))

    def __str__(self):
        return self.user.username



class Demand(models.Model):
    """ Model for request """
    SERVICE_CHOICES =(
        ("Normal","Normal"),
        ("Express","Express")
    )
    IS_ACTIVE_CHOICES =(
        ("IN PROGRESS","In progress"),
        ("PICKED","Picked"),
        ("DELIVERED","Delivered")
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    service = models.CharField(verbose_name=_('Type of delivery'),max_length=7, choices=SERVICE_CHOICES, default='Normal')
    name = models.CharField( verbose_name=_('Full name'),max_length=50 )
    phone = PhoneField(verbose_name=_('Phone'))
    autocomplete = AddressField(verbose_name=_('Address'))
    email = EmailField(verbose_name=_('Email'))
    description = RichTextField(verbose_name=_('Description'))
    is_active = models.CharField(default='IN PROGRESS', choices=IS_ACTIVE_CHOICES, max_length=11)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}" 

    


class Driver(models.Model):
    """ Model for deliver """
    deliver = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.deliver.get_full_name()


class Mandat(models.Model):
    """ Model for deliver dispatching """
    STATUS_CHOICES =(
        ("DELIVERED","Delivered"),
        ("NOT_DELIVERED","Not delivered")
    )
    colis = models.OneToOneField(Demand, on_delete=models.CASCADE, related_name='demand')
    mandataire = models.ManyToManyField(Driver, related_name='driver')
    statut = models.CharField(max_length=13, choices = STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}"
