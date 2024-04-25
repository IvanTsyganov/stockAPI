from rest_framework import serializers

from mainapp.models import Stock, Category, Equipment
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'role', 'equipments')


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ('id', 'stock_info')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'category_info')


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ('id', 'amount', 'category', 'stock', 'user')
