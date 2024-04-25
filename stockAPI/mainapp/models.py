from django.db import models
from users.models import User


class Stock(models.Model):
    stock_info = models.CharField(
        max_length=256,
        verbose_name='Информация о складе',
        help_text='Укажите информацию о складе.'
    )

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class Category(models.Model):
    category_info = models.CharField(
        max_length=256,
        verbose_name='Информация о категории',
        help_text='Укажите информацию о категории.'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Equipment(models.Model):
    amount = models.SmallIntegerField(
        verbose_name='Количетво оборудования',
        help_text='Укажите количетво оборудования',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='equipments')

    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        verbose_name='Склад',
        related_name='equipments')

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    def __str__(self):
        return self.amount
