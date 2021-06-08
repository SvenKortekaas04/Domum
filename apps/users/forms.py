from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from apps.users import models

# User settings
AppearanceSettingsForm = forms.modelform_factory(models.Settings, fields=("theme",))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]