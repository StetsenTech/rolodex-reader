"""Modules handles setting up pytest configurations"""
import pytest


@pytest.fixture(scope="module")
def invalid_entries():
    invalid = [
        "Jamie, James, 826901156, 912 871 6927, brown",
        "0.123412341234",
        "Moose, Slick, (123)-45678-91234567, black, 92561",
    ]

    return invalid

@pytest.fixture(scope="module")
def valid_entries():
    valid = [
        "Cruickshank, Bonita, (703)-742-0996, Blue, 10013",
        "Zoe Yundt, Red, 85487, 351 341 9108",
        "Shannon, Collier, 57296, 521 142 8864, Green",
    ]

    return valid

@pytest.fixture(scope="module")
def mix_entries(valid_entries, invalid_entries):
    mix = valid_entries + invalid_entries
    
    return mix