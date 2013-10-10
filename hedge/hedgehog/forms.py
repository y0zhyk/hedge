from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    """Form for providing user credentials"""
    username = forms.CharField(label="User name", required=False)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)

    def clean(self):
        raise ValidationError("Failed to login")

    def is_valid(self):
        """Verifies user credentials"""
        try:
            import pam
            return pam.authenticate(self.data['username'], self.data['password'])
        except ImportError:
            return False