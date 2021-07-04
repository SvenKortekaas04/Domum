from django.urls import path, include

from apps.api import views


urlpatterns = [
    path("auth/", include('rest_framework.urls')),

    path("users/", views.UsersView.as_view(), name="api_users"),
    path("users/<str:username>/", views.UserView.as_view(), name="api_users_user"),

    path("files", views.FilesView.as_view(), name="api_files"),
    path("files/upload/", views.FileUploadView.as_view(), name="api_files_upload"),

    path("folders", views.FoldersView.as_view(), name="api_folders"),
]