from rest_framework import serializers
from .models import Gateway , Payment
from subscriptions.serializer import PackageSerializer

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('title','description','avatar','create_time','update_time')
        
        
class PaymentSerializer(serializers.ModelSerializer):
    package = PackageSerializer()
    gateway = GatewaySerializer()
    class Meta:
        model = Payment
        fields = ('package','gateway','price','status','phone_number','create_time')        
        