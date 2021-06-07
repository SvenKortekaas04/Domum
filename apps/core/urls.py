from django.urls import path, re_path
from django.views.generic import RedirectView

from apps.core import views


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="core_start"), name="core_index"),
    re_path(r"browse(?:/(?P<path>.*))?/$", views.browse, name="core_browse"),
    path("recent/", views.recent, name="core_recent"),
    path("start/", views.start, name="core_start")
]