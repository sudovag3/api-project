from django.db import models
from django.contrib.auth.models import User

USER = models.ForeignKey(User, on_delete=models.CASCADE)
DATE = models.DateField(verbose_name='Дата')


class AccountsAndCards(models.Model):
    user = USER
    account_name = models.TextField(verbose_name='Название счета')
    balance_on_start = models.IntegerField(verbose_name='Баланс на старте')
    credit_limit = models.PositiveIntegerField(verbose_name='Кредитный лимит')
    date_start = models.DateField(verbose_name='Дата создания')
    def __str__(self):
        return f'#{self.user} {self.account_name} {self.balance_on_start} {self.credit_limit}'

    class Meta:
        verbose_name        = 'Счет(карта)'
        verbose_name_plural = 'Счета и карты'


class Transfers(models.Model):
    user = USER
    date = DATE
    withdrawal_amount = models.PositiveIntegerField(verbose_name='Сумма списания')
    deposit_amount = models.PositiveIntegerField(verbose_name='Сумма пополнения')
    from_the_account = models.ForeignKey(AccountsAndCards, related_name='from+',
                                         on_delete=models.CASCADE, verbose_name='Со счёта')
    on_the_account = models.ForeignKey(AccountsAndCards, related_name='to',
                                       on_delete=models.CASCADE, verbose_name='На счёт')

    class Meta:
        verbose_name        = 'Перемещение'
        verbose_name_plural = 'Перемещения'


class ReferenceTypes(models.Model):
    user = USER
    type_name = models.TextField(verbose_name='Название типа')

    class Meta:
        verbose_name        = 'Справочник(Тип)'
        verbose_name_plural = 'Справочник(Типы)'


class ReferenceViews(models.Model):
    WEEK = 'WE'
    MOUNTH = 'MO'
    REGULARITY = (
        (WEEK, 'Week'),
        (MOUNTH, 'Mounth'),
    )
    type = models.ForeignKey(ReferenceTypes, on_delete=models.CASCADE, verbose_name='Тип')
    view_name = models.TextField(verbose_name='Название вида')
    regularity = models.CharField(max_length=2, choices=REGULARITY, null=True)
    is_income = models.BooleanField(verbose_name='Это доход?')

    class Meta:
        verbose_name        = 'Справочник(Вид)'
        verbose_name_plural = 'Справочник(Виды)'


class Expenses(models.Model):
    user = USER
    date = DATE
    amount = models.PositiveIntegerField(verbose_name='Сумма')
    description = models.TextField(verbose_name='Описание')
    expense = models.ForeignKey(ReferenceViews, on_delete=models.SET_NULL, verbose_name='Расход', null=True)
    account = models.ForeignKey(AccountsAndCards, on_delete=models.CASCADE, verbose_name='Счёт')

    class Meta:
        verbose_name        = 'Расход'
        verbose_name_plural = 'Расходы'


class Incomes(models.Model):
    user = USER
    date = DATE
    amount = models.PositiveIntegerField(verbose_name='Сумма')
    description = models.TextField(verbose_name='Описание')
    income = models.ForeignKey(ReferenceViews, on_delete=models.SET_NULL, verbose_name='Доход', null=True)
    account = models.ForeignKey(AccountsAndCards, on_delete=models.CASCADE, verbose_name='Счёт')

    class Meta:
        verbose_name        = 'Доход'
        verbose_name_plural = 'Доходы'


class Depreciations(models.Model):
    user = USER
    name = models.TextField(verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    date_buy = models.DateField(verbose_name='Дата покупки')
    service_time = models.PositiveIntegerField(verbose_name='Срок гарантии')
    sum_final = models.PositiveIntegerField(verbose_name='Отложено')

    class Meta:
        verbose_name        = 'Амортизация'
        verbose_name_plural = 'Амортизация'


class FinancialPlan(models.Model):
    date = DATE
    user = USER

    class Meta:
        verbose_name        = 'Финплан'
        verbose_name_plural = 'Финплан'


class FinancialPlanItems(models.Model):
    financial_plan = models.ForeignKey(FinancialPlan, on_delete=models.CASCADE)
    plan = models.PositiveIntegerField(verbose_name='План')
    fact = models.PositiveIntegerField(verbose_name='Факт')
    result_of_week = models.IntegerField(verbose_name='Результат недели', null=True)

    class Meta:
        verbose_name        = 'Финплан(пункт)'
        verbose_name_plural = 'Финплан(пункт)'