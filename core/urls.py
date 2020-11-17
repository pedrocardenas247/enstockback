from django.urls import path, include
from . import views
from rest_framework import routers
from .views import index

router = routers.DefaultRouter()
router.register('Full_Categories', views.CategoryFullViewset)
router.register('Full_Stores', views.StoreFullViewset)
router.register('Full_ListStores', views.ListStoresSerializerViewset)

urlpatterns = [
    path('', index, name='index'),
    path('apis/', include(router.urls))
]
