from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from domum.const import (
    NAME,
    THEME_DARK,
    THEME_LIGHT
)


class User(AbstractUser):
    """User model."""

    storage_path = models.CharField(
        unique=True,
        max_length=150,
        blank=False,
    )
    storage_id = models.CharField(
        unique=True,
        max_length=16,
        blank=False,
    )


class Settings(models.Model):
    """User settings."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings", blank=True)

    # Appearance
    theme = models.CharField(max_length=8, choices=[(theme, theme.capitalize()) for theme in (THEME_DARK, THEME_LIGHT)], default=THEME_LIGHT)

