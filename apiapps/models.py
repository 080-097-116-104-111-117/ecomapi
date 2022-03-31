from tokenize import Name
from django.db import models

from setuptools import Require
from rest_framework import serializers


from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, default_address, mobile, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, default_address, mobile, password, **other_fields)

    def create_user(self, email, user_name, default_address, mobile, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          default_address= default_address, mobile = mobile, password = password, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    default_address = models.CharField(max_length=60, null=True, default=None, blank=True)
    mobile = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=150, unique=True)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','default_address', 'mobile']

    def __str__(self):
        return self.user_name


# class NameUpperField(models.CharField):
#     def __init__(self, *args, **kwargs):
#         # self.is_uppercase = kwargs.pop('uppercase', False)
#         super(NameUpperField, self).__init__(*args, **kwargs)
    
#     def getValue(self, model_instance, add):
#         value = getattr(model_instance, self.attname, None)
#         if value:
#             value = value.upper()
#             print(value)
#             setattr(model_instance, self.attname, value)
#             return value
        
#         else:
#             return super(NameUpperField, self).getValue(model_instance, add)
        
class ProductCategory(models.Model):
    name = models.CharField(max_length=50, default=None, blank=True, unique=True)
    # name = NameUpperField(max_length=50)
    description = models.TextField(max_length=200)
    

    def __str__(self):
        return self.name[0].upper() + self.name[1:]



class product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    offer_price = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to ='images/', default=None, blank=True)
    stock = models.IntegerField(default=1)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


# class card(models.Model):
#     product = models.ForeignKey(product, on_delete=models.CASCADE)
#     customer = models.ForeignKey(customer, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)

#     def __str__(self):
#         return self.product.name


class address(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name
        

class customer(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=30, null=True, blank=True )
    Password = models.CharField(max_length=20, null=True, blank=True)
    default_address = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.IntegerField()
    # card_id = models.ForeignKey(card, on_delete=models.CASCADE, null = True, blank = True)
    address = models.ForeignKey(address, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.Name




class order(models.Model):
    product = models.ManyToManyField(product)
    customer = models.ForeignKey(NewUser, related_name="user", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50)

    def __str__(self):
        # return self.product.id
        return self.customer.Name
