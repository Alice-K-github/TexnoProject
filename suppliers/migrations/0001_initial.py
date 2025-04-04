# Generated by Django 5.1.7 on 2025-03-31 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('country', models.CharField(max_length=20, verbose_name='страна')),
                ('city', models.CharField(max_length=20, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=20, null=True, verbose_name='улица')),
                ('house_number', models.PositiveIntegerField(blank=True, max_length=5, null=True, verbose_name='номер дома')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, null=True, verbose_name='Название продукта')),
                ('model', models.CharField(blank=True, null=True, verbose_name='Название модели')),
                ('product_launch_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Название')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='Задолженность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.contacts', verbose_name='Контакты')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.products', verbose_name='Продукты')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.suppliers', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
    ]
