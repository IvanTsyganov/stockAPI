# Generated by Django 2.2.19 on 2024-04-24 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_info', models.CharField(help_text='Укажите информацию о категории.', max_length=256, verbose_name='Информация о категории')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_info', models.CharField(help_text='Укажите информацию о складе.', max_length=256, verbose_name='Информация о складе')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.SmallIntegerField(help_text='Укажите количетво оборудования', verbose_name='Количетво оборудования')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='mainapp.Category', verbose_name='Категория')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='mainapp.Stock', verbose_name='Склад')),
            ],
        ),
    ]
