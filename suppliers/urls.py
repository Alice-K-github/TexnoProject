from django.contrib import admin
from django.urls import path
from suppliers.models import Suppliers
from suppliers.serializers import SuppliersSerializer
from suppliers.views import SuppliersListAPIView, SuppliersRetrieveAPIView, SuppliersCreateAPIViewAPIView, \
    SuppliersUpdateAPIView, SuppliersDestroyAPIView

app_name = 'suppliers'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('suppliers/', SuppliersListAPIView.as_view(
        queryset=Suppliers.objects.all(),
        serializer_class=SuppliersSerializer),
        name='suppliers_list'),
    path('suppliers/<int:pk>/', SuppliersRetrieveAPIView.as_view(
        queryset=Suppliers.objects.all(),
        serializer_class=SuppliersSerializer),
        name='suppliers_Retrieve'),
    path('suppliers/new/', SuppliersCreateAPIViewAPIView.as_view(
        queryset=Suppliers.objects.all(),
        serializer_class=SuppliersSerializer),
        name='suppliers_Create'),
    path('suppliers/<int:pk>/update/', SuppliersUpdateAPIView.as_view(
        queryset=Suppliers.objects.all(),
        serializer_class=SuppliersSerializer),
        name='suppliers_Update'),
    path('suppliers/<int:pk>/delete/', SuppliersDestroyAPIView.as_view(
        queryset=Suppliers.objects.all(),
        serializer_class=SuppliersSerializer),
        name='suppliers_Destroy'),
]
