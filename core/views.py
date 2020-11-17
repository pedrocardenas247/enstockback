from django.http import HttpResponse
from django.shortcuts import render
from .serializers import CategorySerializer, StoresSerializer, ListStoresSerializer
from rest_framework import viewsets, generics
from .models import Categories, Store
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
import json
import pyrebase


with open('config.json', 'r') as file:
    config = json.load(file)
firebase = pyrebase.initialize_app(config['config_firebase'])
database = firebase.database()


def index(request):
    template_name = "index.html"
    return render(request, template_name)


def get_default_store():
    return Store.objects.get(name="title")


class CategoryFullViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class StoreFullViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoresSerializer
    permission_classes = (AllowAny,)


class ListStoresSerializerViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = ListStoresSerializer
    permission_classes = (AllowAny,)