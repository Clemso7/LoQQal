# Generated by Django 3.1.11 on 2021-12-29 03:36

import address.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('delivery', '0007_auto_20211004_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='business_address',
            field=models.CharField(blank=True, help_text='Business or home address', max_length=300, null=True, verbose_name='Business or home address'),
        ),
        migrations.AlterField(
            model_name='author',
            name='business_name',
            field=models.CharField(blank=True, help_text='Business name or Username', max_length=100, null=True, verbose_name='Business name or Username'),
        ),
        migrations.AlterField(
            model_name='author',
            name='business_phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Business or personal phone', max_length=31, null=True, verbose_name='Business or personal phone'),
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='author',
            name='user_type',
            field=models.CharField(choices=[('Individual', 'Individual'), ('Compagny', 'Compagny')], default='Individual', max_length=10, verbose_name='Person or Compagny'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='autocomplete',
            field=address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, to='address.address', verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='is_active',
            field=models.CharField(choices=[('IN PROGRESS', 'In progress'), ('PICKED', 'Picked'), ('DELIVERED', 'Delivered')], default='In progress', max_length=11),
        ),
        migrations.AlterField(
            model_name='demand',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='phone',
            field=phone_field.models.PhoneField(max_length=31, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='service',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Express', 'Express')], default='Normal', max_length=7, verbose_name='Type of delivery'),
        ),
    ]
