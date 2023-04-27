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
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        package_id = request.query_params.get('package')
        gateway_id = request.query_params.get('gateway')
        try:
            package_t = Package.objects.get(pk=package_id,is_enable=True)
            gateway_t = Gateway.objects.get(pk=gateway_id,is_enable=True)
        except (Package.DoesNotExist,Gateway.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        payment_o = Payment.objects.create(
            user=request.user,
            package=package_t,
            gateway=gateway_t,
            price=package_t.price,
            phone_number=request.user.phone_number,
            token=str(uuid.uuid4())
        )
        return Response({'token':payment_o.token,'Bank-url':'http://bank-url.com','callback_url':'http://my-site.com/payments/pay/'})
    
    def post(self,request):
        token = request.data.get('token')
        st = request.data.get('status')
        try:
            payment = Payment.objects.get(token=token)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if st != 10:
            pass
                
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
        
        
        
