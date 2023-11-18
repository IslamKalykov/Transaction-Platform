from django.urls import path
from .views import AccountTransactionView, AccountDetailView


urlpatterns = [
    path('transactions/', AccountTransactionView.as_view(), name='transaction_list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail')
]


