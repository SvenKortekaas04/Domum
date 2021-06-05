from django.urls import path

from apps.api import views


urlpatterns = [
    path("users/", views.UsersView.as_view()),
    path("users/<str:username>", views.UserView.as_view())
]