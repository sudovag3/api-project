from rest_framework import serializers
from rest_framework import generics
from .models import *
from .serializers import CreateModelSerializer

CT_MODEL_MODEL_CLASS = {
    'accounts_and_cards': AccountsAndCards,
    'transfers': Transfers,
    'reference_types': ReferenceTypes,
    'reference_views': ReferenceViews,
    'expenses': Expenses,
    'incomes': Incomes,
    'depreciations': Depreciations,
    'financial_plan_items': FinancialPlanItems

}


class ParameterView:
    def dispatch(self, request, *args, **kwargs):
        self._model = CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        return super().dispatch(request, *args, **kwargs)

    def get_serializer_class(self):
        CreateModelSerializer.Meta.model = self._model
        return CreateModelSerializer


