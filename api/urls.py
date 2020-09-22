from django.contrib import admin
from django.urls import path, include
from .v1 import urls as v1_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(v1_urls)),
]
