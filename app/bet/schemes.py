from marshmallow import Schema, fields, validate


class BetSchema(Schema):
    id = fields.Int(required=False)
    user_id = fields.Int(required=True)
    instrument = fields.Str(required=True)
    time_frame = fields.Str(required=True)
    price = fields.Float(required=True)
    direction = fields.Str(required=True)
    create_data = fields.Str(required=True)


class BetResponceSchema(Schema):
    data = fields.Nested(BetSchema)


class BetRequestSchema(Schema):
    user_id = fields.Int(required=True)
    instrument = fields.Str(required=True)
    time_frame = fields.Str(required=True)
    price = fields.Float(required=True)
    direction = fields.Str(required=True)
    create_data = fields.Str(required=True)
