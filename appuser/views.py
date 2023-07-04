from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import AppUserSerialzier


User = get_user_model()


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = AppUserSerialzier(users, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = AppUserSerialzier(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

