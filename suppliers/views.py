from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import BasePermission, IsAuthenticated

from suppliers.models import Suppliers
from suppliers.serializers import SuppliersSerializer


# Проверка активности пользователя
class Is_active(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        else:
            return False


# Список поставщиков
class SuppliersListAPIView(generics.ListAPIView):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
    # Фильтр\поиск по определённым странам поставщиков
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']
    # Разрешения
    permission_classes = [Is_active, IsAuthenticated]


# Детали объекта поставщика
class SuppliersRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
    permission_classes = [Is_active, IsAuthenticated]


# Создание нового объекта поставщика
class SuppliersCreateAPIViewAPIView(generics.CreateAPIView):
    serializer_class = SuppliersSerializer
    permission_classes = [Is_active, IsAuthenticated]


# Редактирование\обновление объекта поставщика
class SuppliersUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
    permission_classes = [Is_active, IsAuthenticated]


# Удаление объекта поставщика
class SuppliersDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
    permission_classes = [Is_active, IsAuthenticated]
