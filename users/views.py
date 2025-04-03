from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView
from users.forms import CustomUserCreationForm
from users.serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Аутентификация пользователя
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('')


# Выход пользователя
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'
    success_url = reverse_lazy('')


# Регистрация пользователя
class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')


# Представление токена
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
