"""Module that adds methods to help with processing input"""
import re

import phonenumbers

# Regex validators for file input
VALID_ONE = re.compile((
    r'(?P<last>[A-z]+),\s(?P<first>[A-z. ]+),\s'
    r'(?P<phone>\([0-9]{3}\)-[0-9]{3}-[0-9]{4}),\s'
    r'(?P<color>[A-z ]+),\s(?P<zip>[0-9]{5})'
))
VALID_TWO = re.compile((
    r'(?P<first>[A-z. ]+)\s(?P<last>[A-z]+),\s'
    r'(?P<color>[A-z ]+),\s(?P<zip>[0-9]{5}),\s'
    r'(?P<phone>[0-9]{3}\s[0-9]{3}\s[0-9]{4})'
))
VALID_THREE = re.compile((
    r'(?P<first>[A-z. ]+),\s(?P<last>[A-z]+),\s'
    r'(?P<zip>[0-9]{5}),\s(?P<phone>[0-9]{3}\s[0-9]{3}\s[0-9]{4}),\s'
    r'(?P<color>[A-z ]+)'
))

def process_entries(entries, p_format="{}-{}-{}"):
    """Checks if entry data is valid

    Args:
        entries(list): List of personal information
        p_region(basestring): Region the phone is from
        p_format(basestring): Output format for phone number
    Returns:
        list, list: List of entry dictories and a list of invalid indices
    """
    valid_entries = [] # Tracks valid entries
    errors = [] # Tracks invalid entry indices

    for i, entry in enumerate(entries):
        # Check to see if entry is valid
        # If invalid, add index to list of invalid entries
        if VALID_ONE.match(entry):
            entry_match = VALID_ONE.match(entry)
        elif VALID_TWO.match(entry):
            entry_match = VALID_TWO.match(entry)
        elif VALID_THREE.match(entry):
            entry_match = VALID_THREE.match(entry)
        else:
            errors.append(i)
            continue

        # Convert phone number
        # @ TODO: Handle in marshmallow schema
        phone = _format_phone_number(entry_match.group("phone"), p_format)

        # Check to see if entry is valid
        entry_dict = {
            "first_name": entry_match.group("first"),
            "last_name": entry_match.group("last"),
            "phone_number": phone,
            "color": entry_match.group("color"),
            "zipcode": entry_match.group("zip")
        }

        valid_entries.append(entry_dict)

    return valid_entries, errors

def _format_phone_number(phone, p_format):
    """Converts phone number to desired format"""
    phone_object = phonenumbers.parse(phone, "US")
    return phonenumbers.format_number(phone_object, p_format)
