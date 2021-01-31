from django.contrib import admin
from django.urls import path, include

from base.views import *

app_name = 'bases'
urlpatterns = [

    path('create/<str:ct_model>', CreateView.as_view()),
    path('show/<str:ct_model>', ListView.as_view()),
    path('detail/<str:ct_model>/<int:pk>', DetailView.as_view()),
    path('balance', get_balance_from_currently_date),
    path('bdr', get_bdr_from_currently_date)
]
