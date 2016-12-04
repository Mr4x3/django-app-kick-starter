# Python Imports

# Django Imports
from django.contrib.auth import authenticate
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

# Third Party Django Imports

# Inter App Imports

# Local Imports
from .models import {{app_name | title}}


# Forms For {{app_name | title}}
class {{app_name | title}}Form(forms.ModelForm):
    """
    Create A {{app_name | title}} Form.
    """

    class Meta:
        model = {{app_name | title}}
        fields = ('field',)
        widgets = {
            'field': forms.Textarea,
        }

    def __init__(self, *args, **kwargs):
        pass
