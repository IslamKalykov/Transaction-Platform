from django.urls import path

from user import views

urlpatterns = [
    path("register-user/", views.RegisterUserAPIView.as_view(), name="register_user")
]