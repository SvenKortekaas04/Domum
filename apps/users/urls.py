from django.contrib.auth.views import LoginView
from django.urls import path

from apps.users import views


urlpatterns = [
    path("account/delete", views.delete_account, name="users_account_delete"),

    path("login/", LoginView.as_view(template_name="users/login.html"), name="users_login"),
    path("logout/", views.logout, name="users_logout"),
    path("register/", views.RegisterView.as_view(), name="users_register"),

    # User settings
    path("settings/account/", views.AccountSettingsView.as_view(), name="users_settings_account"),
    path("settings/appearance/", views.AppearanceSettingsView.as_view(), name="users_settings_appearance"),
    path("settings/security/", views.SecuritySettingsView.as_view(), name="users_settings_security")
]