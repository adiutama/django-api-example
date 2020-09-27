from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from dynamic_rest.viewsets import DynamicModelViewSet

from .serializer import (
  UserSerializer,
  GroupSerializer
)


class UserViewSet(DynamicModelViewSet):
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class GroupViewSet(DynamicModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
