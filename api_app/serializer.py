from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import RecipesInfo


class RecipesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipesInfo
        fields = "__all__"
