import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.core.util.storage import (
    get_files,
    get_subdirs,
    paths_from_root_to_path
)


class BrowseView(LoginRequiredMixin, TemplateView):
    """
    Browse through all files and folders.
    """

    template_name = "core/storage/browse.html"

    def get(self, request, username, path: str = None):
        if not request.user.username == username:
            pass  # Raise error

        # Compose a path
        path = os.path.join(request.user.storage_path, os.path.normcase(path)) if path else request.user.storage_path

        # Set extra context
        context = self.get_context_data(
            files=get_files(path, user=request.user),
            subdirs=get_subdirs(path, user=request.user),
            breadcrumb=[(os.path.relpath(path, request.user.storage_path), os.path.split(path)[1]) for path in paths_from_root_to_path(root=request.user.storage_path, end=path)]
        )

        return render(request, self.template_name, context)


class RecentView(LoginRequiredMixin, TemplateView):
    """
    Render recently opened files and folders.
    """

    template_name = "core/recent.html"


@login_required
def action_download(request):
    pass


@login_required
def action_delete(request):
    pass


@login_required
def action_rename(request):
    pass
