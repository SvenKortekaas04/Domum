from django.urls import path

from apps.api import views


urlpatterns = [
    path("users/", views.UsersView.as_view(), name="api_users"),
    path("users/<str:username>", views.UserView.as_view(), name="api_users_user")
]