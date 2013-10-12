from django import forms
from django.core.exceptions import ValidationError
from django.forms.util import ErrorList


class _ErrorList(ErrorList):

    def __unicode__(self):
        if not self:
            return u''
        return u'{}'.format(self[0])


class LoginForm(forms.Form):
    """Form for providing user credentials"""
    username = forms.CharField(label="User name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, **kwds):
        super(LoginForm, self).__init__(error_class=_ErrorList, empty_permitted=True, **kwds)

    def clean(self):
        raise ValidationError("Failed to login")

    def is_valid(self):
        """Verifies user credentials"""
        try:
            import pam
            return pam.authenticate(self.data['username'], self.data['password'])
        except ImportError:
            return False