from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfile_maanger(BaseUserManager):
    """Manager for user Profiles"""
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('Please enter a email address')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_super_user(self,email,name,password):
        """create and save anew  super user with a given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database Model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfile_maanger()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['name']

    def get_full_name(self):
        """retrive full name of user"""
        return self.name
    def get_short_name(self):
        """retrive short name"""
        return self.name
    def __str__(self):
        "return sring representation of our user"
        return self.email
