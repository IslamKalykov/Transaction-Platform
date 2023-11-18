from django.urls import path
from .views import TransactionListView


urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    # Другие URL-маршруты вашего приложения...
]