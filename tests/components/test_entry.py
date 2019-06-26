"""Module handles tests for the entry component"""
import json

import pytest

from rolodex.components.entry import EntryComponent


@pytest.fixture(scope="function")
def entry_component():
    """Creates an instance of the entry component"""
    return EntryComponent()

def test_create_ouput(entry_component, mix_entries):
    """Tests creating output from entry dictionary"""
    # Check fixtures
    assert isinstance(entry_component, EntryComponent)
    assert isinstance(mix_entries, list)
    assert mix_entries
    assert len(mix_entries) == 6

    # Attempt to use component then  check to see if
    # the result is a json string
    print(mix_entries)
    result = entry_component.create_output(mix_entries)
    assert isinstance(result, basestring) 
    
    # Check to see if json string is formatted properly
    json_dict = json.loads(result)

    assert isinstance(json_dict, dict)
    assert json_dict.get("entries")
    assert len(json_dict['entries']) == 3
    assert json_dict.get("errors")
    assert len(json_dict['errors']) == 3

    # Check entries to see if they have the correct keys
    for entry in json_dict["entries"]:
        assert entry.get("firstname")
        assert entry.get("lastname")
        assert entry.get("phonenumber")
        assert entry.get("zipcode")
        assert entry.get("color")
 

    assert json_dict['errors'] == [3,4,5]