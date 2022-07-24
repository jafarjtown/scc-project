from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields =  "__all__" 