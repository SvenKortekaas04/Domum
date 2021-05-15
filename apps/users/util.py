import os
import secrets
from typing import (
    Tuple
)

from django.conf import settings

from apps.users.models import Settings, User


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


def init_user(first_name: str, last_name: str, email: str, password: str) -> User:
    """Initialize a new user."""

    # Initialize storage
    storage_path, storage_id = init_user_storage()

    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, storage_path=storage_path, storage_id=storage_id)

    # Assign user specific settings
    settings = Settings.objects.create(user=user)
    settings.save()

    return user