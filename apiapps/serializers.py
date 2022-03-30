from rest_framework import serializers
from . models import product
from . models import customer
from . models import order
from . models import ProductCategory

from .models import NewUser


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

class productserializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields = '__all__'
        depth = 1


class userserializer(serializers.ModelSerializer):

    class Meta:
        model = customer
        fields = '__all__'


class orderserializer(serializers.ModelSerializer):

    class Meta:
        model = order
        fields = '__all__'
        #depth = 1


class catagoryserializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'
