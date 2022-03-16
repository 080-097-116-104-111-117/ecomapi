import imp
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import product
from . models import customer
from . models import order
from .models import  ProductCategory
from .serializers import productserializer
from .serializers import userserializer
from .serializers import orderserializer
from .serializers import catagoryserializer


class productList(APIView):

    def get(self, request):
        product1 = product.objects.all()
        serializer = productserializer(product1, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        pass


class customerList(APIView):

    def get(self, request):
        customer1 = customer.objects.all()
        serializer = userserializer(customer1, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        pass


class orderList(APIView):

    def get(self, request):
        order1 = order.objects.all()
        serializer = orderserializer(order1, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        pass


class productCatagoryList(APIView):

    def get(self, request):
        product1 = ProductCategory.objects.all()
        serializer = catagoryserializer(product1, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        pass

