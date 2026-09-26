from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.user_info, name="user_info"),
    path("register/", views.register, name="register_user"),
    path("login/", views.login, name="login_user"),
    path("profile/", views.get_profile, name="profile_user"),
    path("logout/", views.logout, name="logout_user"),
]