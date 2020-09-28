from django.urls import include, path
from rest_framework import routers

from .views import (
  UserViewSet,
  GroupViewSet,
  TokenObtainPairView,
  TokenRefreshView
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'token/', TokenObtainPairView.as_view()),
    path(r'token/refresh/', TokenRefreshView.as_view()),
]
