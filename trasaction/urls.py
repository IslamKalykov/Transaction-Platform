from django.urls import path
from .views import TransactionListView, AccountDetailView


urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail')
]


