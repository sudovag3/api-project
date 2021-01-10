from django.shortcuts import render
from rest_framework import generics
from base.serializers import *
from base.models import AccountsAndCards
from .services import ParameterView


# Create your views here.


class CreateView(ParameterView, generics.CreateAPIView):
    """
    Api view для создания моделей
    """


class DetailView(ParameterView, generics.RetrieveUpdateDestroyAPIView):

    """
    Api view для изменения моделей
    """

    def get_serializer_class(self):
        CreateModelSerializer.Meta.model = self._model
        return CreateModelSerializer

    def get_queryset(self):
        queryset = self._model.objects.all()
        return queryset


class ListView(ParameterView,generics.ListAPIView):
    """
    Api view для просмотра моделей
    """

    def get_queryset(self):
        """
        Фильтрация по id пользователя
        """
        queryset = self._model.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset




