from django.contrib import admin
from suppliers.models import Suppliers, Contacts, Products
from django.urls import reverse
from django.utils.html import format_html


@admin.action(description="Очистить задолженность")
def Clean(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Suppliers)
class SuppliersUserAdmin(admin.ModelAdmin):
    list_display  = (
        "id",
        "name",
        "contacts",
        "products",
        "debt",
        'created_at',
        'activity_link'
    )
    list_filter = ['contacts__city']
    actions = [Clean]
    def activity_link(self, obj):
        if obj.supplier:
            link = reverse("admin:suppliers_suppliers_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier)
        else:
            return None

    activity_link.short_description = 'Поставщик'


@admin.register(Contacts)
class ContactsUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "country",
        "city",
        "street",
        'house_number',
    )

@admin.register(Products)
class ProductsUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "model",
        "product_launch_date",
    )
