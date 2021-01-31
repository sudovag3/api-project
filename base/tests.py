# from django.test import TestCase
# from .models import AccountsAndCards, Transfers, FinancialPlanItems, FinancialPlan
# from django.contrib.auth import get_user_model
# User = get_user_model()
# # Create your tests here.
#
# class CardsTransferCases(TestCase):
#
#     def setUp(self) -> None:
#         self.user = User.objects.create(username = 'testuser',
#                                         password = 'password')
#         self.card1 = AccountsAndCards.objects.create(user = self.user,
#                                                      account_name = 'test account 1',
#                                                      balance_on_start = 10000,
#                                                      credit_limit = 0)
#         self.card2 = AccountsAndCards.objects.create(user = self.user,
#                                                      account_name = 'test account 2',
#                                                      balance_on_start = 20000,
#                                                      credit_limit = 0)
#
#         self.transfer = Transfers.objects.create(user = self.user,
#                                                  withdrawal_amount = 13000,
#                                                  deposit_amount = 10000,
#                                                  from_the_account = self.card1,
#                                                  on_the_account = self.card2)
#
#         def get(balance)