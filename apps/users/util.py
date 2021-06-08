import os
import secrets
import shutil
from typing import (
    Tuple
)

from django.conf import settings
from django.contrib.auth import get_user_model

from apps.users.models import Settings


def create_storage_id() -> str:
    """Create a unique storage ID for a user."""

    storage_id = secrets.token_hex(4)
    return storage_id


def init_user_storage() -> Tuple[str]:
    """Initialize a user's storage."""

    # Create a unique storage ID
    storage_id = create_storage_id()

    # Create a storage path
    storage_path = os.path.join(settings.STORAGE_DIR, "users", storage_id)

    # Create directories
    os.makedirs(storage_path)

    return storage_path, storage_id


def init_user(username: str, first_name: str, last_name: str, email: str, password: str):
    """Initialize a new user."""

    # Initialize storage
    storage_path, storage_id = init_user_storage()

    User = get_user_model()
    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password, storage_path=storage_path, storage_id=storage_id)

    # Assign user specific settings
    settings = Settings.objects.create(user=user)
    settings.save()

    return user


def delete_user(username: str) -> None:
    """Delete a user."""

    User = get_user_model()
    user = User.objects.get(username=username)
    user.delete()

    # Delete storage
    shutil.rmtree(user.storage_path)