"""Modules handles tests for the process utility """

from rolodex.utils.process import process_entries

def test_process_entries(mix_entries):
    """Test processing a set of entries"""
    entries, errors = process_entries(mix_entries)
    assert len(entries) == 3
    assert len(errors) == 3

    for entry in entries:
        assert entry.get("first_name")
        assert entry.get("last_name")
        assert entry.get("phone_number")
        assert entry.get("zipcode")
        assert entry.get("color")

    for error in errors:
        assert isinstance(error, int)

def test_process_valid_entries(valid_entries):
    """Test processing only valid entries"""
    entries, errors = process_entries(valid_entries)
    assert len(entries) == 3
    assert len(errors) == 0
    assert errors == []

def tests_process_invalid_entries(invalid_entries):
    """Test processing only invalid entries"""
    entries, errors = process_entries(invalid_entries)
    assert len(entries) == 0
    assert len(errors) == 3
    assert entries == []
