from django.urls import path,include
from .models import Package,Subscription
from .views import PackageListView,SubscriptionView

urlpatterns = [
    path('package/',PackageListView.as_view()),
    path('sub/',SubscriptionView.as_view()),
]