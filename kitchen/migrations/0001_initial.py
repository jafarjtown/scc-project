# Generated by Django 4.0.2 on 2022-07-31 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.FloatField()),
                ('quanity', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='kitchen.category')),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_foods', models.ManyToManyField(related_name='kitchen_available', to='kitchen.Food')),
                ('foods', models.ManyToManyField(related_name='kitchen_offered', to='kitchen.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kitchen.food')),
                ('kitchen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordered', to='kitchen.kitchen')),
            ],
        ),
    ]
