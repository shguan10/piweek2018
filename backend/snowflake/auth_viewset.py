from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django import forms

from django.db.models.signals import post_save
from snowflake.fridge_viewset import Fridge


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

        
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class SignupViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request : Request, format=None):
        form = SignUpForm(request.data)
        try:
            form.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=raw_password)            
            auth.login(request, user)
            
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except:
            return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)


class SigninViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request : Request, format=None):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        return Response({'message': 'Supplied credentials did not match a valid user'}, status=status.HTTP_401_UNAUTHORIZED)


class SignoutViewSet(APIView):
    permission_classes = [AllowAny]
    def get(self, request: Request, format=None):
        auth.logout(request)
        return Response()


def save_profile(sender, instance, created, **kwargs):
    if created:
        Fridge.objects.create(user=instance)

post_save.connect(save_profile, sender=User)
