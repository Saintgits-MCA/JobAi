from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserSettings
from django.contrib.auth.models import User
from .models import Company


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ["dark_mode", "email_notifications", "two_factor_auth"]
        widgets = {
            "dark_mode": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "email_notifications": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "two_factor_auth": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Old Password"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="New Password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Confirm New Password"
    )

class UploadFileForm(forms.Form):
    file = forms.FileField()