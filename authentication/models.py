from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

ACCOUNT_TYPE = (
    ('SF', 'Staff'),
    ('ST', 'Student'),
    ('OT', 'Other'),
)

class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    phone_no = models.CharField(max_length=15)
    account_type = models.CharField(choices=ACCOUNT_TYPE, default=ACCOUNT_TYPE[1], max_length=5)
    account_id = models.CharField(max_length=50)
    #to know wether account is kitchen or customers
    is_kitchen = models.BooleanField(default=False)
    pass