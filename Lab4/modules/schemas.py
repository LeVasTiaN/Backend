from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    user_id = fields.Int(load_default=None) 

class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    category_id = fields.Int(required=True)
    amount = fields.Float(required=True)
    created_at = fields.DateTime(dump_only=True)