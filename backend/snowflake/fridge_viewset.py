from rest_framework import status
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated

from snowflake.serializers import FridgeSerializer
from snowflake.models import Fridge
import requests


class FridgeViewSet(viewsets.GenericViewSet):
    serializer_class = FridgeSerializer

    # Define name for the view
    def get_view_name(self):
        return "Fridges"

    def get_queryset(self):
        return Fridge.objects.all()

    def get_permissions(self):
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    # Get Fridge
    def list(self, request : Request):
        try:
            fridge = Fridge.objects.all().filter(user=request.user).get()
            serializer = FridgeSerializer(fridge)
            return Response(serializer.data)
        except Fridge.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND);

    @list_route(methods=['POST'], url_path='add')
    def add(self, request: Request):
        fridge = Fridge.objects.all().filter(user=request.user).get()
        # some parsing shit here.....

        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    @list_route(methods=['POST'], url_path='delete')
    def delete(self, request: Request):
        fridge = Fridge.objects.all().filter(user=request.user).get()
        # some parsing shit here.....

        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)

    @list_route(methods=['GET'], url_path='recipes')
    def recipes(self, request: Request):
        try:
            fridge = Fridge.objects.all().filter(user=request.user).get()
            items = fridge.items.all().distinct('name')
            ingredients = [item.name for item in items]

            APP_ID = '842672fb'
            APP_KEY = '59aff2597b0f7689a7619a17b1a537d0'
            B_APP_ID = 'd355f4b8'
            B_APP_KEY = 'b41d10565e4c3a436eab0a5b148fa428'
            URL = 'https://api.edamam.com/search'

            query = ','.join(ingredients)
            param = {'q': query, 'app_id': APP_ID, 'app_key': APP_KEY, 'to':20}
            r = requests.get(URL, params=param)
            if r.status_code == 200:
                return Response(r.json())
            param = {'q': query, 'app_id': B_APP_ID, 'app_key': B_APP_KEY, 'to':20}
            r = requests.get(URL, params=param)
            if r.status_code == 200:
                return Response(r.json())
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Fridge.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @list_route(methods=['GET'], url_path='aggregates')
    def aggregates(self, request: Request):
        try:
            fridge = Fridge.objects.all().filter(user=request.user).get()
            
            map = {}
            items = fridge.items.all()
            for item in items:
                if map.get(item.name, None):
                    map[item.name] = map[item.name] + 1
                else:
                    map[item.name] = 1
                    
            return Response(map)
        except Fridge.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND);
