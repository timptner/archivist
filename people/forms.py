import re

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'faculty', 'username')
        help_texts = {
            'email': _("Only email addresses with 'st.ovgu.de' are allowed."),
            'username': _("Please use the same username as you have for your university account."),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        pattern = r'^((\w+\.)?\w+)@((st\.)?ovgu\.de)$'
        if not re.match(pattern, data):
            raise ValidationError(
                _("You did not use 'st.ovgu.de' as the email domain."),
                code='forbidden',
            )

        return data
