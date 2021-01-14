from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework import serializers
from rest_framework import generics
from django.http import JsonResponse
from .models import *
from .serializers import CreateModelSerializer
from typing import Dict,List

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


def get_balance_from_date(to_date: str, account_id: int, from_date: str = '', res: int = 0) -> List[int]:
    """
    Функция, высчитывающая данные о счете по конкретным датам
    :param to_date: До какой даты проводить расчёты
    :param account_id: id счета, для которого проводим расчёты
    :param from_date: От какой даты проводить расчёты, если мы ее не указываем, считается с момента создания счёта
    :param res: Итоговый баланс на счёте в to_date
    :return: List [конечный баланс, суммарный доход, суммарный расход]
    """

    account = AccountsAndCards.objects.get(id=account_id)
    income_sum = 0
    expense_sum = 0
    if from_date == '':
        from_date = account.date_start
    if res == 0:
        res = account.balance_on_start - account.credit_limit


    income_sum += Incomes.objects.filter(date__range=[from_date,
                                                      to_date],
                                         account = account).aggregate(sum = Coalesce(Sum('amount'), 0))['sum']

    income_sum += Transfers.objects.filter(date__range=[from_date,
                                                        to_date],
                                           on_the_account=account).aggregate(sum = Coalesce(Sum('deposit_amount'), 0))['sum']

    res += income_sum

    res -= Expenses.objects.filter(date__range=[from_date,
                                                to_date],
                                   account = account).aggregate(sum = Coalesce(Sum('amount'),
                                                                               0))['sum']
    expense_sum += Expenses.objects.filter(date__range=[from_date,
                                                        to_date],
                                           account = account).aggregate(sum = Coalesce(Sum('amount'),
                                                                                       0))['sum']

    res -= Transfers.objects.filter(date__range=[from_date,
                                                 to_date],
                                    from_the_account=account).aggregate(sum = Coalesce(Sum('deposit_amount'),
                                                                                       0))['sum']

    expense_sum += Transfers.objects.filter(date__range=[from_date,
                                                         to_date],
                                            from_the_account=account).aggregate(sum = Coalesce(Sum('deposit_amount'),
                                                                                       0))['sum']

    return [res, income_sum, expense_sum]


def get_balance(from_date: str, to_date: str, user_id: int) -> JsonResponse:
    """
    Функция, формирующая dict c выходными данными баланса по дате
    :param from_date: От какой даты
    :param to_date: До какой даты
    :param user_id: Id пользователя, для которого считается баланс
    :return: dict
    """
    res = {}

    for i in AccountsAndCards.objects.filter(user=user_id):
        print(i.account_name)
        start_sum = get_balance_from_date(to_date=from_date, account_id=i.id)[0]
        sum_date = get_balance_from_date(to_date=to_date, account_id=i.id, from_date= from_date, res=start_sum)
        res.update({
            f'{i.id}': {
                'name': i.account_name,
                'on_start': start_sum,
                'income': sum_date[1],
                'expense': sum_date[2],
                'on_end': sum_date[0],
            }
        })


    return JsonResponse(res)
