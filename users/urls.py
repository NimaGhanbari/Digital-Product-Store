from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
#from .serializer import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/',RegisterView.as_view()),
    #path('get-token/',get_token.as_view()),
    path('profile/',ProfileView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/', MyTokenObtainPairSerializer.get_token(user), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]