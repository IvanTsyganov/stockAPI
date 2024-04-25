from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import CategoryViewSet, StockViewSet, EquipmentViewSet


router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='categories')
router.register('stocks', StockViewSet, basename='stocks')
router.register(r'stocks/(?P<stock_id>\d+)/equipments',
                EquipmentViewSet, basename='equipments')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
