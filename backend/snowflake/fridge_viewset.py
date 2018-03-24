from rest_framework import status
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated

from snowflake.serializers import FridgeSerializer
from snowflake.models import Fridge


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
        fridge = Fridge.objects.all().filter(user=request.user).get()
        serializer = FridgeSerializer(fridge)
        return Response(serializer.data)

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

    @list_route(methods=['GET'], url_path='quantity')
    def quantity(self, request: Request):
        fridge = Fridge.objects.all().filter(user=request.user).get()

        if request.query_params.get('item', None):
            item_name = request.query_params.get('item')
            item = fridge.items.filter(name=item_name).get()
            return Response({'quantity': item.quantity})

        quantity = 0
        for item in fridge.items:
            quantity += item.quantity

        return Response({'quantity': quantity})
