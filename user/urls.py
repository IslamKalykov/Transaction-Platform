from django.urls import path

from user import views

urlpatterns = [
    path("register-user/", views.RegisterUserAPIView.as_view(), name="register_user"),
    path("authenticate-user/", views.LoginUserAPIView.as_view(), name="authenticate_user")
]