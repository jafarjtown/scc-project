from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, phone_no, name, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    if not phone_no:
        raise ValueError('Users must have a phone number')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        name = name,
        phone_no = phone_no,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, name, phone_no, password, **extra_fields):
    return self._create_user(email, password, False, False, phone_no, name, **extra_fields)

  def create_superuser(self, email, name, phone_no, password, **extra_fields):
    user=self._create_user(email, password, True, True, phone_no, name, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    phone_no = models.BigIntegerField(max_length=13) # Added Field
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=False) # Added Field
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_no']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)