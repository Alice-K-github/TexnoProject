from django.template.context_processors import request
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import BasePermission, IsAuthenticated

from suppliers.models import Suppliers
from suppliers.serializers import SuppliersSerializer


class Is_active(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.filter(is_acrive=True).exists():
            print(request.user)
            return True
        else:
            print(request.user)
            return False


class SuppliersListAPIView(generics.ListAPIView):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['contacts__country']
    '''permission_classes = [Is_active, IsAuthenticated]'''


class SuppliersRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
    permission_classes = [Is_active, IsAuthenticated]


class SuppliersCreateAPIViewAPIView(generics.CreateAPIView):
    serializer_class = SuppliersSerializer
    permission_classes = [Is_active, IsAuthenticated]


class SuppliersUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
    permission_classes = [Is_active, IsAuthenticated]


class SuppliersDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SuppliersSerializer
    queryset = Suppliers.objects.all()
    permission_classes = [Is_active, IsAuthenticated]

