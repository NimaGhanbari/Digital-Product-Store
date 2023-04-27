#Django
from django.shortcuts import render

#local
from .models import Gateway,Payment
from .serializer import GatewaySerializer

from subscriptions.models import Package,Subscription

#Rest Framework
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import requests
import uuid


class GatewayListView(APIView):
    def get(self,request):
        Gateways = Gateway.objects.filter(is_enable=True)
        serialized = GatewaySerializer(Gateways,many = True)
        return Response(serialized.data)
   
    
class PaymentView(APIView):
    #این خط برای آن است که برای ساخت آبجکت پیمنت نیاز است که کاربر ما مشخص باشد
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        #ذهنیت این بخش آن است که یک ابجکت از پیمت ساخته شود و برای بانک ارسال شود 
        
        #در اینجا ما نوع گیت وی و نوع پکیج را برایمان کاربر از طریق ریکوئست میفرستد
        package_id = request.query_params.get('package')
        gateway_id = request.query_params.get('gateway')
        #ما میریم درون دیتابیس وآن پکیج و گیت وی رو میریزیم تو متغیر .چون برای ساخت ابجکت پیمن نیاز است
        try:
            package_t = Package.objects.get(pk=package_id,is_enable=True)
            gateway_t = Gateway.objects.get(pk=gateway_id,is_enable=True)
        except (Package.DoesNotExist,Gateway.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        #حال که تمام اطلاعات برای ساخت شی پیمنت را داریم یک شی میسازیم و برای بانک آن توکن شی را ارسال میکنیم
        payment_o = Payment.objects.create(
            user=request.user,
            package=package_t,
            gateway=gateway_t,
            price=package_t.price,
            phone_number=request.user.phone_number,
            token=str(uuid.uuid4())
        )
        #اللبته ما این توکن و آدرس بانک وآدرس کالبک را به کاربر ارسال میکنیم و خود کاربر وقتی روی لینک میزند به سمت بانک با اطلاعاتی که 
        #دریافت کرده میرود و بعد از اتمام کار به سمت سرور ما با آدرس کالبک بر میگردد 
        return Response({'token':payment_o.token,'Bank-url':'http://bank-url.com','callback_url':'http://my-site.com/payments/pay/'})
    
    def post(self,request):
        #ذهنیت این بخش آن است که وقتی کابر آدرس کالبک را کلیک کرد به این تابع بیاید
        #به طور کلی بانک در کالبک یکسری اطلاعات را به ما میدهد که در اینجا فرض شده یک کد وضعیتی را با همان توکن ارسالی برای ما میفرستد
        token = request.data.get('token')
        st = request.data.get('status')
        #آن پیمنت را با همان توکن دریافتی درون یک میتغیر میریزیم
        try:
            payment = Payment.objects.get(token=token)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #خود بانک به ما میگه که مثلا اگر استاتوس برابر 10 بود پرداخت اوکیه
        if st != 10:
            pass
        
        
        #حال علاوه بر اینکه ما یکبار چک کردیم که اوکی است وضعیت پرداخت ما یک وریفای از دوباره به بانک ارسال میکنیم که مطمعن شویم همه چی اوکیه
        #این ریکوئست با ریکوئست های قبلی فرق میکند و این یک پکیجی است که یک آدرس اینترنتی را با فرمت دلخواهش صدا میزند .یکجورایی مثل 
        #اچرف در اچ تی ام ال می باشد
        r = request.post('bank-verify-url',data={})
        if r.status_code != 200:
            pass
        
        payment.status = payment.STATUS_PAID
        payment.save()
        
        Subscription.objects.create(
            user=payment.user,
            package=payment.package,
            expaire_time=timezone.now() + timezone.timedelta(days=payment.package.duration.days)
        )
        
        return Response({'detail':'payment is successful'})
        
        
        
