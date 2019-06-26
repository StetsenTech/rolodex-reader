"""Module hands methods that relate to rolodex entries"""

from rolodex.schemata.entry import OutputSchema
from rolodex.utils.process import process_entries

class EntryComponent(object):
    """Class that handles rolodex entry methods"""

    def create_output(self, data, sort=False, indent=4):
        """Generates an output based on given data

        Args:
            data(list): List of rolodex entries
            sort(bool): Whether or not to sort result
            indent(int): Number of spaces for indent
        Returns:
            basestring: JSON converted dictionary from schema
        """
        entries, errors = process_entries(data)
       
        schema = OutputSchema()

        output = {
            "entries": entries,
            "errors": errors
        }

        return schema.dumps(output, sort_keys=sort, indent=indent).data
