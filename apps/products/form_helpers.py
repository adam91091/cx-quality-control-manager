import re
from typing import Dict

from apps.validators import REGEXPS


def format_form_values(data: Dict[str, str]) -> Dict[str, str]:
    """
    Update form values:
    - change any commas in numeric fields into dots
    :param data:    Dictionary with form field names and string values
    :return         Formatted data dict
    """
    for val in data:
        if re.match(REGEXPS['common']['num_field'], data[val]):
            data[val] = data[val].replace(',', '.')
    return data
