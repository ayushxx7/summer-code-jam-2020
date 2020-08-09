from django.http import Http404
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.AllowAny]
