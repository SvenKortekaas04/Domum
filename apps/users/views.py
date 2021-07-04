from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from apps.users.forms import (
    AppearanceSettingsForm,
    UserRegisterForm,
    UserUpdateForm
)
from apps.users.models import Settings
from apps.users.util import init_user, delete_user


@login_required
def logout(request):
    """Log a user out."""

    auth_logout(request)  # Log the user out

    messages.success(request, "You have been logged out.")
    return redirect("users_login")


class RegisterView(FormView):
    """
    Register a user.
    """

    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_login")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]

        # Create a new user
        init_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

        # Flash a message stating that an account has 
        # been created and redirect the user to the login page
        messages.success(self.request, "Your account has been created.")

        return super().form_valid(form)


@login_required
def delete_account(request):
    """Delete an account."""

    delete_user(username=request.user.username)  # Delete a user

    return redirect("users_login")


class AccountSettingsView(LoginRequiredMixin, FormView):
    """
    Render user account settings.
    """

    template_name = "users/settings/account.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("users_settings_account")

    def get(self, request) -> HttpResponse:
        form = self.form_class(instance=request.user)

        # Get context data
        context = self.get_context_data(form=form)

        return render(request, self.template_name, context)

    def post(self, request) -> HttpResponse:
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            
            # Flash a message stating that the user's account has 
            # been updated and redirect the user to the settings page
            messages.success(self.request, "Your account has been updated.")

            return super().form_valid(form)
        else:
            return super().form_invalid(form)


class AppearanceSettingsView(LoginRequiredMixin, FormView):
    """
    Render user appearance settings.
    """

    template_name = "users/settings/appearance.html"
    form_class = AppearanceSettingsForm
    success_url = reverse_lazy("users_settings_account")

    def get(self, request) -> HttpResponse:
        # Retrieve user settings
        settings = Settings.objects.get(user=request.user)
        form = self.form_class(instance=settings)

        # Get context data
        context = self.get_context_data(form=form)

        return render(request, self.template_name, context)

    def post(self, request) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            # Save changes
            settings = Settings.objects.get(user=request.user)

            for key, value in form.cleaned_data.items():
                setattr(settings, key, value)

            settings.save()
            
            # Flash a message stating that the user's account has 
            # been updated and redirect the user to the settings page
            messages.success(self.request, "Your account has been updated.")

            return super().form_valid(form)
        else:
            return super().form_invalid(form)


class SecuritySettingsView(LoginRequiredMixin, FormView):
    """
    Render user security settings.
    """

    template_name = "users/settings/security.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("users_settings_account")

    def get(self, request) -> HttpResponse:
        form = self.form_class(request.user)
        
        # Get context data
        context = self.get_context_data(form=form)

        return render(request, self.template_name, context)

    def post(self, request) -> HttpResponse:
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            form.save()
            
            # Flash a message stating that the user's account has 
            # been updated and redirect the user to the settings page
            messages.success(self.request, "Your account has been updated.")

            return super().form_valid(form)
        else:
            return super().form_invalid(form)