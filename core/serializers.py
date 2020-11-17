from rest_framework import serializers, request
from .models import Categories, Store, ProductStore


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['title', 'address', 'lat', 'lon', 'category', 'logo_host', 'description', 'payments', 'email',
                  'phoneNum', 'owner', 'dni', 'ruc', 'website', 'facebook', 'instagram', 'img1host', 'img2host',
                  'img3host', 'img4host', 'img5host', 'img6host', 'video', 'verified', 'slug', 'activate']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['title', 'description', 'icon_host', 'slug', 'activate']


class ProductStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStore
        fields = ['title', 'slug', 'brand', 'material', 'colors', 'sizes', 'price', 'img1host', 'quantity',
                  'description', 'store']


class ListStoresSerializer(serializers.ModelSerializer):
    category_match = StoresSerializer(many=True, read_only=True)
    store_match = ProductStoreSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['title', 'description', 'icon_host', 'slug', 'category_match', 'store_match']
