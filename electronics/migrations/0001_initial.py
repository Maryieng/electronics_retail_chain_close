# Generated by Django 5.0.2 on 2024-07-16 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('create_data', models.DateField(verbose_name='Дата выхода на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_level', models.PositiveIntegerField(choices=[(0, 'Завод'), (1, 'Магазин'), (2, 'Индивидуальный предприниматель')], verbose_name='Тип')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('country', models.CharField(max_length=150, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер дома')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('debt', models.FloatField(blank=True, default=0.0, null=True, verbose_name='задолженность перед поставщиком')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='electronics.link', verbose_name='Поставщик')),
                ('products', models.ManyToManyField(default=None, to='electronics.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
    ]