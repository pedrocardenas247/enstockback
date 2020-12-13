from rest_framework import serializers, request
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Categories, Store, ProductStore, Customer, CategoriesProd, Ubicacion
from django.contrib.auth.models import User, Group
from rest_framework_gis.serializers import GeoFeatureModelSerializer


# Serializers de los usuarios


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        return token


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['userImg', 'userImg', 'address', 'phoneNum', 'dni', 'groups']


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                                        email=validated_data['email'])
        return user


# # Serializer de las tiendas

class LocationStoreSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ubicacion
        geo_field = "location"
        # id_field = False
        fields = ['location']

        # def get_properties(self, instance, fields):
        #     # This is a PostgreSQL HStore field, which django maps to a dict
        #     return instance.metadata


class ProductStoreSerializer(serializers.ModelSerializer):
    point_prod_match = LocationStoreSerializer(many=True, read_only=True)

    class Meta:
        model = ProductStore
        fields = ['id', 'title', 'slug', 'brand', 'material', 'colors', 'sizes', 'price', 'img1host',
                  'img2host', 'img3host', 'quantity',
                  'description', 'point_prod_match']


class CategoriesProdSerializer(serializers.ModelSerializer):
    catego_match = ProductStoreSerializer(many=True, read_only=True)

    class Meta:
        model = CategoriesProd
        fields = ['id', 'title', 'description', 'icon_host', 'slug', 'catego_match']


class StoresSerializer(serializers.ModelSerializer):
    storeTop_match = CategoriesProdSerializer(many=True, read_only=True)
    point_match = LocationStoreSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['id', 'title', 'address', 'category', 'logo_host', 'description', 'payments', 'email',
                  'phoneNum', 'ruc', 'website', 'facebook', 'instagram', 'short_description',
                  'img1host', 'img2host', 'img3host', 'img4host', 'img5host', 'img6host', 'video', 'verified',
                  'slug', 'activate', 'point_match', 'storeTop_match']


class CategorySerializer(serializers.ModelSerializer):
    category_match = StoresSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'title', 'description', 'icon_host', 'slug', 'activate', 'react_icon', 'category_match']
