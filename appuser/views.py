from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import AppUserSerialzier


User = get_user_model()


class UserList(generics.ListCreateAPIView):
    """
    Get all users or create new user
    """
    queryset = User.objects.all()
    serializer_class = AppUserSerialzier


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get a user, update it or delete it
    """
    queryset = User.objects.all()
    serializer_class = AppUserSerialzier
