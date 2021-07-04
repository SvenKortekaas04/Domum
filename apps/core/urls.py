from django.urls import path, re_path
from django.views.generic import RedirectView

from apps.core import views


urlpatterns = [
    path("", RedirectView.as_view(pattern_name="core_recent"), name="core_index"),

    re_path(r"^browse/(?P<username>.+)/(?P<path>.*)/$", views.BrowseView.as_view(), name="core_browse"),
    re_path(r"^browse/(?P<username>.+)/$", views.BrowseView.as_view(), name="core_browse"),

    path("recent/", views.RecentView.as_view(), name="core_recent")
]