from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CategoriesProdSerializer, StoresSerializer, CategorySerializer, \
    ProductStoreSerializer, MyTokenObtainPairSerializer
from rest_framework import viewsets, filters
from .models import Categories, Store, CategoriesProd, ProductStore
from rest_framework.permissions import AllowAny, IsAuthenticated


def index(request):
    template_name = "index.html"
    return render(request, template_name)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = (AllowAny,)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class ProductStoreViewSet(viewsets.ModelViewSet):
    queryset = ProductStore.objects.all()
    serializer_class = ProductStoreSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ["title",]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    permission_classes = (AllowAny,)


class CategoriesProdViewSet(viewsets.ModelViewSet):
    queryset = CategoriesProd.objects.all()
    serializer_class = CategoriesProdSerializer
    permission_classes = (AllowAny,)


class StoreFullViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoresSerializer
    permission_classes = (AllowAny,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


