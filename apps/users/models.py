from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import pytz

from domum.const import (
    NAME,
    THEME_DARK,
    THEME_LIGHT,
    UNIT_SYSTEM_IMPERIAL,
    UNIT_SYSTEM_METRIC
)


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email, and password."""

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_staff=True.'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must have is_superuser=True.'
            )

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User model."""

    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into '
            'this admin site.'
        ),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be '
            'treated as active. Unselect this instead '
            'of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        _('date joined'),
        default=timezone.now,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name'
    ]


class AdminSettings(models.Model):
    """Admin settings."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="admin_settings", blank=True)

    # General
    house_name = models.CharField(max_length=16, default=NAME)
    unit_system = models.CharField(max_length=8, choices=[(unit_system, unit_system.capitalize()) for unit_system in (UNIT_SYSTEM_IMPERIAL, UNIT_SYSTEM_METRIC)], default=UNIT_SYSTEM_METRIC)

    # Location
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)


class Settings(models.Model):
    """User settings."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings", blank=True)

    # Appearance
    theme = models.CharField(max_length=8, choices=[(theme, theme.capitalize()) for theme in (THEME_DARK, THEME_LIGHT)], default=THEME_LIGHT)

