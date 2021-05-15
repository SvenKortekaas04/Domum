import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.core.util.storage import (
    get_files,
    get_subdirs,
    paths_from_root_to_path
)


@login_required
def browse(request, path: str = None):
    # Compose a path
    path = os.path.join(request.user.storage_path, os.path.normcase(path)) if path else request.user.storage_path

    context = {
        "files": get_files(path, user=request.user),
        "subdirs": get_subdirs(path, user=request.user),
        "breadcrumb": [(os.path.relpath(path, request.user.storage_path), os.path.split(path)[1]) for path in paths_from_root_to_path(root=request.user.storage_path, end=path)]
    }

    return render(request, "core/storage/browse.html", context=context)


@login_required
def recent(request):
    return render(request, "core/storage/recent.html")
