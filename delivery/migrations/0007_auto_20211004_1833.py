# Generated by Django 3.1.11 on 2021-10-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_auto_20211004_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='service',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Express', 'Express')], default='Normal', max_length=7),
        ),
    ]
