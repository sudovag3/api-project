from rest_framework import serializers
from base.models import *




class CreateModelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания Моделей
    """

    class Meta:
        model = None
        fields = '__all__'



