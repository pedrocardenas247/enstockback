from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models.signals import post_save
from django.dispatch import receiver


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.",
            'token': str(refresh.access_token),
            'ok': "true",

        })

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            instance.groups.add(Group.objects.get(name='customer'))
