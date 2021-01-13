from django.contrib import admin
from .models import *
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

admin.site.register(AccountsAndCards)
admin.site.register(ReferenceTypes)
admin.site.register(ReferenceViews)
admin.site.register(Incomes)
admin.site.register(Expenses)
admin.site.register(Depreciations)
admin.site.register(FinancialPlan)
admin.site.register(FinancialPlanItems)
admin.site.register(Transfers)

# Register your models here.
# @admin.register(Incomes)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'date', 'date', 'amount', 'description', 'income', 'account')
#
# @admin.register(Expenses)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'date', 'date', 'amount', 'description', 'expense', 'account')
# @admin.register(ReferenceViews)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'date', 'date', 'amount', 'description', 'expense', 'account')