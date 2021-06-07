from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.users import views


urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="users_login"),
    path("logout/", views.logout, name="users_logout"),
    path("register/", views.register, name="users_register"),

    # User settings
    path("settings/account/", views.settings_account, name="users_settings_account"),
    path("settings/appearance/", views.settings_appearance, name="users_settings_appearance"),
    path("settings/security/", views.settings_security, name="users_settings_security")
]