from django.db import models
from django.contrib import admin
from django.contrib import auth


class Fridge(models.Model):
    user = models.OneToOneField(auth.get_user_model(), on_delete=models.CASCADE)


class FridgeAdmin(admin.ModelAdmin):
    pass


class Item(models.Model):
    name = models.TextField()
    quantity = models.IntegerField()
    date_entered = models.DateTimeField(auto_now_add=True)

    fridge = models.ForeignKey('Fridge', on_delete=models.CASCADE, related_name='items')


class ItemAdmin(admin.ModelAdmin):
    pass
