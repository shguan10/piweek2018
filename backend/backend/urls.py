from django.urls import path, re_path, include
from rest_framework import routers
from snowflake.viewset import FridgeViewSet
from . import admin


router = routers.SimpleRouter()
router.register(r'api/fridge', FridgeViewSet, base_name='Fridge')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # re_path(r'^(?!media).*$', renderer.render_index)
]