# Generated by Django 4.0.2 on 2022-08-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantservice',
            name='name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
