from django.urls import path, include
from .api import RegisterApi
from rest_framework import routers
from .views import index, CategoriesProdViewSet, StoreFullViewset, CategoryViewSet, ProductStoreViewSet

app_name = 'core'


router = routers.DefaultRouter()
# router.register('users', UserViewSet)
router.register('products_store', ProductStoreViewSet)
router.register('catego_pro', CategoriesProdViewSet)
router.register('storeTop_match', StoreFullViewset)
router.register('category_match', CategoryViewSet)
# router.register('Full_ListStores', views.ListStoresSerializerViewset)

urlpatterns = [
    path('', index, name='index'),
    path('apis/', include(router.urls)),
    path('api/register', RegisterApi.as_view()),
]
