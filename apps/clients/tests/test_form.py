from django.test import TestCase

from .factories import ClientFactory
from apps.clients.forms import ClientForm
from apps.constants import CLIENT_SAP_DIGITS
from ...unittest_helpers import get_random_int_with_digit_count


class ClientFormTest(TestCase):
    def setUp(self) -> None:
        self.client = ClientFactory()
        self.valid_client_form_data = {'client_sap_id': str(get_random_int_with_digit_count(CLIENT_SAP_DIGITS)),
                                       'client_name': 'test_client'}
        self.invalid_client_sap_ids = ['0', str(get_random_int_with_digit_count(CLIENT_SAP_DIGITS - 1)),
                                       str(get_random_int_with_digit_count(CLIENT_SAP_DIGITS + 1)), 'test']

    def test_form_sap_id_validation_positive(self):
        client_form = ClientForm(data=self.valid_client_form_data, instance=self.client)
        self.assertTrue(client_form.is_valid(), msg=f"Value: {self.valid_client_form_data['client_sap_id']}")

    def test_form_sap_id_validation_negative(self):
        for value in self.invalid_client_sap_ids:
            self.valid_client_form_data['client_sap_id'] = value
            client_form = ClientForm(data=self.valid_client_form_data, instance=self.client)
            self.assertFalse(client_form.is_valid(), msg=f"Value: {value}")
