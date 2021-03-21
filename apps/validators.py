from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator

from apps.constants import CLIENT_SAP_DIGITS, PRODUCT_SAP_DIGITS, ORDER_SAP_DIGITS, USERNAME_LENGTH

REGEXPS = {
    'common': {'num_field': r'^([0-9]*|[0-9]*(\.|,)\d+)$',
               'int_field': r'^[0-9]*$', },
    'client': {'client_sap_id': r'^([0-9]{' + str(CLIENT_SAP_DIGITS) + '})$', },
    'product': {'product_sap_id': r'^([0-9]{' + str(PRODUCT_SAP_DIGITS) + '})$',
                'index': r'^$|^(T|R)([0-9]{9})/([0-9]{2})$'},
    'order': {'order_sap_id': r'^([0-9]{' + str(ORDER_SAP_DIGITS) + '})$', },
    'user': {'username': r'^([a-z]{' + str(USERNAME_LENGTH) + ')$',
             'password': r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', }
}


class CxUsernameValidator(UnicodeUsernameValidator):
    regex = REGEXPS['user']['username']


def validate_client_sap_id():
    return RegexValidator(regex=REGEXPS['client']['client_sap_id'],
                          message=f"Numer SAP klienta powinien składać się z dokładnie {CLIENT_SAP_DIGITS} cyfr",
                          code='invalid sap id')


def validate_product_sap_id():
    return RegexValidator(regex=REGEXPS['product']['product_sap_id'],
                          message=f"Numer SAP produktu składać się z dokładnie {PRODUCT_SAP_DIGITS} cyfr",
                          code='invalid sap id')


def validate_index():
    return RegexValidator(regex=REGEXPS['product']['index'],
                          message="Indeks produktu powinien być w określonym formacie, np. T1034321/26",
                          code='invalid index')


def validate_order_sap_id():
    return RegexValidator(regex=REGEXPS['order']['order_sap_id'], message="Numer partii powinien składać się z "
                                                                          f"dokładnie {ORDER_SAP_DIGITS} cyfr",
                          code='invalid sap id')


def validate_num_field():
    return RegexValidator(regex=REGEXPS['common']['num_field'],
                          message="Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową")


def validate_int_field():
    return RegexValidator(regex=REGEXPS['common']['int_field'],
                          message="Pole integer powinno zawierać liczbę całkowitą")


def validate_username():
    return RegexValidator(regex=REGEXPS['user']['username'],
                          message=f"Login powinien składać się z dokładnie {USERNAME_LENGTH} małych liter")
