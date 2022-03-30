import imp
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from . models import product
from . models import customer
from . models import order
from .models import  ProductCategory
from .serializers import productserializer
from .serializers import userserializer
from .serializers import orderserializer
from .serializers import catagoryserializer

CREATE_SUCCESS = 'created'

from rest_framework.exceptions import AuthenticationFailed
from .models import NewUser
from .serializers import NewUserSerializer
import jwt, datetime

class CustomUser(APIView):
    def get_queryset(self):
        user = NewUser.objects.all()
        return user
    

    def get(self, request, id =None):
        if id:
            user = NewUser.objects.get(id=id)
            serializer = NewUserSerializer(user, context={"request":request})
            return Response(serializer.data)

        user = self.get_queryset()
        serializer = NewUserSerializer(user, many=True, context={"request":request})
        # print(serializer.data)
        return Response(serializer.data)
         

        
    def post(self, request):
        serializer = NewUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Login(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user =NewUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('email  is incorrect!!')

        if  user.password == password:
            raise AuthenticationFailed('password is incorrect!!')

        payload = {
            'id' : user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days = 365),
            'iat' : datetime.datetime.utcnow()
        }

        print(datetime.timedelta(days = 365))

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        
        response.set_cookie(key='token', value=token, httponly=True)

        response.data = {
            'token' : token
        }

        return response

        # return Response({
        #     'token' : token
        # })
 

class UsersView(APIView):
    
    def get(self, request):
        token = request.COOKIES.get('token')
        # print(request.data)

        if not token:
            raise AuthenticationFailed('[Unauthenticated]')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms = ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('[Unauthenticated]')

        user = NewUser.objects. filter(id = payload['id']).first()
        serializer = NewUserSerializer(user)

        return Response(serializer.data)


class Logout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'massage': 'success'
        }
        return response
            


class productList(APIView):

    def get(self, request, id=None):
        if id:
            product1 = product.objects.get(id=id)
            serializer = productserializer(product1, context={"request":request})
            return Response(serializer.data)

        product1 = product.objects.all()
        serializer = productserializer(product1, many=True,context={"request":request})
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = productserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def customer_List(request, id =None):
    try:
        customer1 = customer.objects.all()
    except customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if id:
            customer1 = customer.objects.get(id=id)
            serializer = userserializer(customer1, context={"request":request})
            return Response(serializer.data)
        serializer = userserializer(customer1, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = userserializer(data=data)
        data = {}
        if serializer.is_valid():
            new_customer = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['name'] = new_customer.Name
            data['Email'] = new_customer.Email
            data['Password'] = new_customer.Password
            data['default_address'] = new_customer.default_address
            data['Mobile'] = new_customer.Mobile
            return Response(data=data)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
class customerList(APIView):

    def get(self, request):
        customer1 = customer.objects.all()
        serializer = userserializer(customer1, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        pass

"""

class orderList(APIView):

    def get_queryset(self):
        order1 = order.objects.all()
        return order1
    
    def get(self, request, id =None):
        if id:
            order1 = order.objects.get(id=id)
            serializer = orderserializer(order1, context={"request":request})
            return Response(serializer.data)

        order1 = self.get_queryset()
        serializer = orderserializer(order1, many=True, context={"request":request})
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = orderserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    


class productCatagoryList(APIView):

    def get(self, request):
        product1 = ProductCategory.objects.all()
        serializer = catagoryserializer(product1, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        pass

