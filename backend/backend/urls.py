from django.urls import path, re_path, include
from django.http import HttpRequest
from django.shortcuts import render

from rest_framework import routers
from snowflake.fridge_viewset import FridgeViewSet
from snowflake.auth_viewset import SignupViewSet, SigninViewSet, UserSerializer
from . import admin
import json

router = routers.SimpleRouter()
router.register(r'api/fridge', FridgeViewSet, base_name='Fridge')


def render_index(request: HttpRequest):
    user_object = {}
    if request.user:
        serializer = UserSerializer(request.user)
        user_object = serializer.data
    
    json_user = json.dumps(user_object)
    return render(request, "./index.html", context={"user_object": json_user})

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/signup/$', SignupViewSet.as_view()),
    re_path(r'^api/signin/$', SigninViewSet.as_view()),
    re_path(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^$', render_index)
]
