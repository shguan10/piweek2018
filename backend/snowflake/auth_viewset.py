from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class SignupViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request : Request, format=None):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)


class SigninViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request : Request, format=None):
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED)
