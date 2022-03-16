from rest_framework import serializers
from . models import product
from . models import customer
from . models import order
from . models import ProductCategory


class productserializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = '__all__'


class userserializer(serializers.ModelSerializer):

    class Meta:
        model = customer
        fields = '__all__'


class orderserializer(serializers.ModelSerializer):

    class Meta:
        model = order
        fields = ['product_id', 'customer_id', 'quantity', 'address']


class catagoryserializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'