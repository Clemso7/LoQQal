# Generated by Django 3.1.7 on 2021-04-07 00:37

import address.models
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0003_auto_20200830_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsBottomBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Place Your Ad', max_length=200)),
                ('image', models.ImageField(default=None, upload_to='banners/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='AdsRightBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Place Your Ad', max_length=200)),
                ('image', models.ImageField(default=None, upload_to='banners/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='AdsTopBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Place Your Ad', max_length=200)),
                ('image', models.ImageField(default=None, upload_to='banners/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='default-profile-pic.png', null=True, upload_to='uploads/profile-pictures')),
                ('business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('business_phone', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('business_address', address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('description', ckeditor.fields.RichTextField()),
                ('is_active', models.BooleanField(default=False)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.author')),
                ('autocomplete', address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.address')),
            ],
        ),
    ]