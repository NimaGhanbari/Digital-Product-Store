from .models import Package,Subscription
from rest_framework import serializers


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['title','sku','description','avatar','price','duration']
        

class SubscriptionSerializer(serializers.ModelSerializer):
    package = PackageSerializer()
    class Meta:
        model = Subscription
        fields = ['package','created_time','expaire_time']