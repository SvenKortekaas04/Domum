from django.urls import path

from apps.storage import views


urlpatterns = [
    path("", views.index, name="storage_index")
]