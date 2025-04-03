from rest_framework import serializers
from users.models import CustomUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Сериализатор пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_staff', 'is_active']


# Сериализатор для получения токена
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        token['username'] = user.username
        token['email'] = user.email

        return token
