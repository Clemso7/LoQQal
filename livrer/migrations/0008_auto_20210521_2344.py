# Generated by Django 3.1.11 on 2021-05-22 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livrer', '0007_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='objet',
            field=models.CharField(max_length=20),
        ),
    ]