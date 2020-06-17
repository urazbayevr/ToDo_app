from django.contrib import admin
from django.urls import path

from rest_framework import routers
from . import api_views
from django.urls import include, path
from django.contrib import admin

router = routers.DefaultRouter()
router.register('', api_views.TaskViewSet, basename='todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include(router.urls)),
]
