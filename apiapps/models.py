from django.db import models

# Create your models here.
from django.db import models
from setuptools import Require


        
class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    offer_price = models.IntegerField(null=True, blank=True)
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
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.product.name
