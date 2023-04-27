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
        # شماره تلفن را دریافت میکنیم
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        username = request.data.get('username')
        # چک میکنیم که شماره تلفن قبلا ثبت نشده باشد
        # اگر ثبت شده باشد بهش ارور میدهیم البته میتوانیم بخش لاگین را از اینجا ادامه بدهیم
        # اگر ثبت نشده باشد براش یک یوزر درست میکنیم
        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({'error': 'user already registred'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number,password=password,username=username)
        # یک کد رندوم درست میکنیم
        code_random = random.randint(10000, 99999)
        print(code_random)
        # یک دستگاه درست میکنیم . این عمل بیشتر برای آمارگیری بکار می آید
        device = Device.objects.create(user=user)
        # حال کد رندمی که ساختیم را در حافظه ذخیره میکنیم
        cache.set(str(phone_number), code_random, 2*60)
        # حالا این کد را برای همین شماره تلفن اس ام اس میکیم
        # به دلیل محدودیت ما این کد را اس ام اس نمیکنیم بلکه به صورت ریسپانس به کلاینت میفرستیم فقط جهت راه انداختن کار است
        return Response({'code': code_random})



#class get_token(APIView):
#
#    def post(self, request):
#        # حال می اییم و کد فرستاده شده را با کدی که در کش ذخیره کرده بودیم با هم مقایسه میکنیم
#        phone_number = request.data.get('phone_number')
#        code = request.data.get('code')
#        print(code)
#        cashe_code = cache.get(str(phone_number))
#        print(cashe_code)
#        if code != cashe_code:
#            return Response({'error': 'code is invalid'}, status=status.HTTP_400_BAD_REQUEST)
#        # بعد از اینکه کد درست بود ما براش یک توکن درست میکنیم و ارسال میکنیم
#        uuid_code = str(uuid.uuid4())
#        return Response({'uuid_code': uuid_code})
#        # token_pharse = TokenObtainPairView.as_view()
#        # return Response({'token_pharse':token_pharse})



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
