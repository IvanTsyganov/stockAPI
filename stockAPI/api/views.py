from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly
from mainapp.models import Stock, Category, Equipment
from .serializers import StockSerializer, CategorySerializer, EquipmentSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAdminOrReadOnly,)


class EquipmentViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_stock(self):
        return get_object_or_404(Stock, id=self.kwargs.get('stock_id'))

    def get_queryset(self):
        stock_obj = self.get_stock()
        return stock_obj.equipments.all()

    def get_equipment(self):
        return get_object_or_404(Equipment, id=self.kwargs.get('stock_id'))

    def perform_create(self, serializer):
        stock_obj = self.get_stock()
        serializer.save(user=self.request.user, stock=stock_obj)

    def perform_update(self, serializer):
        stock_obj = self.get_stock()
        serializer.save(user=self.request.user, stock=stock_obj)

    def perform_destroy(self, equipment):
        super().perform_destroy(equipment)
