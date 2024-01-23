from .models import Praduct, Category
from rest_framework import serializers


class PraductSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Praduct
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"