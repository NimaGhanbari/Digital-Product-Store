from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import Package,Subscription
from .serializer import PackageSerializer
from rest_framework.response import Response
from .serializer import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.utils import timezone

class PackageListView(APIView):
    def get(self,request):
        packages = Package.objects.filter(is_enable=True)
        serialized = PackageSerializer(packages,many=True)
        return Response(serialized.data)


class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        subuser = request.user
        subs = Subscription.objects.filter(user=subuser,expaire_time__gt=timezone.now())
        serialized = SubscriptionSerializer(subs,many=True)
        return Response(serialized.data)
