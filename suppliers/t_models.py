from django.db import models


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=20, verbose_name='страна')
    city = models.CharField(max_length=20, verbose_name='город')
    street = models.CharField(max_length=20, verbose_name='улица', blank=True, null=True)
    house_number = models.PositiveIntegerField(max_length=5, verbose_name='номер дома', blank=True, null=True)


class Products(models.Model):
    name = models.CharField(verbose_name="Название продукта", blank=True, null=True)
    model = models.CharField(verbose_name="Название модели", blank=True, null=True)
    product_launch_date = models.DateTimeField(blank=True, null=True)


class Factory(models.Model):
    name = models.CharField(verbose_name="Название")
    contacts = models.ManyToManyField(Contacts)
    products = models.ManyToManyField(Products)
    debt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Фабрика'
        verbose_name_plural = 'Фабрики'


class Retail_network(models.Model):
    name = models.CharField(verbose_name="Название")
    contacts = models.ManyToManyField(Contacts)
    products = models.ManyToManyField(Products)
    '''supplier = models.ForeignKey()'''
    debt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class Individual_entrepreneur(models.Model):
    name = models.CharField(verbose_name="Название")
    contacts = models.ManyToManyField(Contacts)
    products = models.ManyToManyField(Products)
    '''supplier = models.ForeignKey()'''
    debt = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField()


    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'
