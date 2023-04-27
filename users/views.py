#Django
from django.shortcuts import render
from django.core.cache import cache

#Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#local 
from .models import User, Device


import random
import uuid


class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        username = request.data.get('username')
        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({'error': 'user already registred'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number,password=password,username=username)
        code_random = random.randint(10000, 99999)
        device = Device.objects.create(user=user)
        cache.set(str(phone_number), code_random, 2*60)
        return Response({'code': code_random})




class ProfileView(APIView):

    def post(self, request):
        user_PhoneNumber = request.data.get('phone_number')
        user = User.objects.get(phone_number=user_PhoneNumber)
        profile = UserProfile.objects.get(user=user)
        return Response({'username': user.username,
                         'first_name': user.first_name,
                         'last_name': user.last_name,
                         'nick-name': profile.nick_name,
                         'email': user.email,
                         'phone_number': user.phone_number,
                         'is_staff': user.is_staff,
                         'is_active': user.is_active,
                         'date_joined': user.date_joined,
                         'last_seen': user.last_seen,
                         # 'avatar':profile.avatar,
                         # 'birthday':profile.birthday,
                         'gender': profile.gender,
                         'province': profile.province.name
                         })
