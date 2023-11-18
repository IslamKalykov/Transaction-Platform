from django.urls import path
<<<<<<< HEAD
from .views import TransactionListView


urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    # Другие URL-маршруты вашего приложения...
=======

from trasaction import views

urlpatterns = [
>>>>>>> e3db745243e2bc4a054a632972fa1b53a993e0aa
]