import copy

from django import forms

from .models import Client
from ..form_styles import CLIENT_SAP_STYLE, BASIC_REQ_STYLE
from ..products.form_helpers import format_form_values
from ..user_texts import ERROR_MSG, LABELS, HINTS


class ClientForm(forms.ModelForm):
    """Provide form for client crud operations
    & hint messages for client side validation.
    """
    validation_hints: dict = HINTS['client']

    def __init__(self, *args, **kwargs):
        if 'data' in kwargs and kwargs['data'] is not None:
            data = format_form_values(copy.deepcopy(kwargs['data']))
            kwargs['data'] = data
        super().__init__(*args, **kwargs)

    class Meta:
        model = Client
        exclude = ()

        labels = LABELS['client']

        widgets = {
            'client_sap_id': forms.TextInput(attrs=CLIENT_SAP_STYLE),
            'client_name': forms.TextInput(attrs=BASIC_REQ_STYLE),
        }

        error_messages = ERROR_MSG['client']
