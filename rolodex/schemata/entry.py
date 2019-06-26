"""Module that handles methods for the entry schema"""

from marshmallow import fields, Schema

class EntrySchema(Schema):
    """Schema for rolodex entry"""
    first_name = fields.String(required=True, dump_to="firstname")
    last_name = fields.String(required=True, dump_to="lastname")
    phone_number = fields.String(required=True, dump_to="phonenumber")
    zipcode = fields.String(required=True)
    color = fields.String(required=True)


class OutputSchema(Schema):
    """Schema for output"""
    entries = fields.Nested(EntrySchema, many=True, required=True, default=[])
    errors = fields.List(fields.Integer(), default=[])
