from django.db import models
from django.db.models import CASCADE


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=20, verbose_name='страна')
    city = models.CharField(max_length=20, verbose_name='город')
    street = models.CharField(max_length=20, verbose_name='улица', blank=True, null=True)
    house_number = models.PositiveIntegerField(verbose_name='номер дома', blank=True, null=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Products(models.Model):
    name = models.CharField(verbose_name="Название продукта", blank=True, null=True)
    model = models.CharField(verbose_name="Название модели", blank=True, null=True)
    product_launch_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Suppliers(models.Model):
    name = models.CharField(verbose_name="Название")
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name="Контакты", blank=True, null=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Продукты", blank=True, null=True)
    debt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True, verbose_name="Задолженность")
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Поставщик", blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
