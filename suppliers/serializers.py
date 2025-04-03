from rest_framework import serializers
from suppliers.models import Contacts, Products, Suppliers


# Сериализатор модели контактов
class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = (
            'email', 'country', 'city', 'street', 'house_number',
        )


# Сериализатор модели продуктов
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'name', 'model', 'product_launch_date',
        )


# Сериализатор модели поставщиков
class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = (
            'name', 'contacts', 'products', 'created_at', 'supplier',
        )
