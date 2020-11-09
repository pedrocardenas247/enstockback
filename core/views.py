from django.http import HttpResponse
from django.shortcuts import render
from .serializers import CategorySerializer
from rest_framework import viewsets, generics
from .models import Categories
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
import json


def index(request):
    template_name = "index.html"
    return render(request, template_name)

class CategoryFullViewset(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


# class RegisterStore(generics.CreateAPIView):
#     def post(self, request, format=None):
#         username=request.data['username']
#         email = request.data['email']
#         password = request.data['password']
#         user = User.objects.create_user(username, email, password)
#         user.save()
#         data = {'detail': 'User save correct!!!!'}
#         reply = json.dumps(data)
#         return HttpResponse(reply, content_type='application/json')