# Generated by Django 3.1.11 on 2021-09-30 17:36

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20210929_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='business_address',
            field=models.CharField(blank=True, help_text='Business or home address', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='business_name',
            field=models.CharField(blank=True, help_text='Business name or Username', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='business_phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Business or personal phone', max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='demand',
            name='service',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Express', 'Express')], default='Normal', max_length=7),
        ),
    ]
