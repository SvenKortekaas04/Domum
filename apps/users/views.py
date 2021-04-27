from django.contrib.auth import logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import redirect, render

from apps.users.forms import (
    AdminSettingsForm,
    AppearanceSettingsForm,
    OnboardingForm,
    UserRegisterForm,
    UserUpdateForm
)
from apps.users.models import AdminSettings, Settings


@login_required
def account(request):
    """Render a the account page of a user."""

    return render(request, "users/account.html")


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
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            # Create a new user and if there is no user, create a superuser
            User = get_user_model()
            if len(User.objects.all()) == 0:
                user = User.objects.create_superuser(first_name=first_name, last_name=last_name, email=email, password=password)
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password)

            # Assign user specific settings
            settings = Settings.objects.create(user=user)
            settings.save()

            if user.is_superuser:
                admin_settings = AdminSettings.objects.create(user=user)
                admin_settings.save()

            # Flash a message stating that an account has 
            # been created and redirect the user to the login page
            messages.success(request, "Your account has been created.")

            if user.is_superuser:
                return redirect("users_onboarding")
            else:
                return redirect("users_login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@user_passes_test(lambda user: user.is_superuser)
def onboarding(request):
    """
    If a superuser has just been registered, this 
    page will be displayed allowing the user to 
    set specific settings for their home.
    """

    if request.method == "POST":
        form = OnboardingForm(request.POST)
        if form.is_valid():
            # Save changes
            admin_settings = AdminSettings.objects.get(user=request.user)

            for key, value in form.cleaned_data.items():
                setattr(admin_settings, key, value)

            admin_settings.save()

            return redirect("frontend_index")
    else:
        # Get superuser
        User = get_user_model()
        superuser = User.objects.filter(is_superuser=True).first()

        # Retrieve user settings
        admin_settings = AdminSettings.objects.get(user=superuser)
        form = OnboardingForm(instance=admin_settings)
    return render(request, "users/onboarding.html", {"form": form})


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
@user_passes_test(lambda user: user.is_superuser)
def settings_admin(request):
    """Render admin settings."""

    if request.method == "POST":
        form = AdminSettingsForm(request.POST)
        if form.is_valid():
            # Save changes
            admin_settings = AdminSettings.objects.get(user=request.user)

            for key, value in form.cleaned_data.items():
                setattr(admin_settings, key, value)

            admin_settings.save()
    else:
        # Get superuser
        User = get_user_model()
        superuser = User.objects.filter(is_superuser=True).first()

        # Retrieve user settings
        admin_settings = AdminSettings.objects.get(user=superuser)
        form = AdminSettingsForm(instance=admin_settings)
    return render(request, "users/settings/admin.html", {"form": form})


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