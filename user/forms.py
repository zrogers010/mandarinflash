from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email address already in use')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "Passwords do not match"
            )

        if len(password2) < 8:
            raise ValidationError(
                "Password must be at least 8 characters long"
            )

        if password2.isdigit():
            raise ValidationError(
                "Password cannot be entirely numeric"
            )

        if any(field.lower() in password2.lower() for field in self.fields):
            raise ValidationError(
                "Password cannot be too similar to your other personal information"
            )

        return password2
