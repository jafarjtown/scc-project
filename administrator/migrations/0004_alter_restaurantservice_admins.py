# Generated by Django 4.0.2 on 2022-08-07 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0003_remove_restaurantservice_admins_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantservice',
            name='admins',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant', to=settings.AUTH_USER_MODEL),
        ),
    ]
