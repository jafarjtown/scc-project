# Generated by Django 4.0.2 on 2022-08-04 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0011_alter_kitchen_foods'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordered',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateField(),
        ),
    ]