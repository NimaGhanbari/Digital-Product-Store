from django.urls import path,include
from .views import GatewayListView,PaymentView

urlpatterns = [
    path('gateway/',GatewayListView.as_view()),
    path('pay/',PaymentView.as_view()),
]