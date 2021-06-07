from django.contrib.auth import logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import redirect, render

from apps.users.forms import (
    AppearanceSettingsForm,
    UserRegisterForm,
    UserUpdateForm
)
from apps.users.models import Settings
from apps.users.util import init_user


@login_required
def logout(request):
    """Log a user out."""

    auth_logout(request)  # Log the user out

    messages.success(request, "You have been logged out.")
    return redirect("users_login")


def register(request):
    """Register a user."""

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            # Create a new user
            user = init_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

            # Flash a message stating that an account has 
            # been created and redirect the user to the login page
            messages.success(request, "Your account has been created.")

            return redirect("users_login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def settings_account(request):
    """Render user account settings."""

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            
            # Flash a message stating that the user's account has 
            # been updated and redirect the user to the settings page
            messages.success(request, "Your account has been updated.")
            return redirect("settings_account")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "users/settings/account.html", {"form": form})


@login_required
def settings_appearance(request):
    """Render user appearance settings."""

    if request.method == "POST":
        form = AppearanceSettingsForm(request.POST)
        if form.is_valid():
            # Save changes
            settings = Settings.objects.get(user=request.user)

            for key, value in form.cleaned_data.items():
                setattr(settings, key, value)

            settings.save()
    else:
        # Retrieve user settings
        settings = Settings.objects.get(user=request.user)
        form = AppearanceSettingsForm(instance=settings)
    return render(request, "users/settings/appearance.html", {"form": form})


@login_required
def settings_security(request):
    """Render user security settings."""

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("settings_account")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "users/settings/security.html", {"form": form})