# Generated by Django 4.0.2 on 2022-07-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('Staff', 'Staff'), ('Student', 'Student'), ('Other', 'Other')], default=('Student', 'Student'), max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.CharField(default='07080332077', max_length=15),
            preserve_default=False,
        ),
    ]
