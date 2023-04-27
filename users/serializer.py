"""from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer,APIView):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['phone_number'] = user.phone_number
        token['code'] = user.code
        # ...
        return token
        """