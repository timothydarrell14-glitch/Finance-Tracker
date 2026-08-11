from extensions import ma
from models.users import Users

from marshmallow.validate import Email
from marshmallow import EXCLUDE, pre_load

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True
        include_fk = True
        unknown = ma.EXCLUDE

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

class UserLoginSchema(UsersSchema):
    class Meta:
        unknown = ma.EXCLUDE

    email = ma.Email(required=True, load_only=True, validate=Email(error="Invalid email address"))
    password = ma.String(required=True, load_only=True)

    @pre_load
    def normalize_email(self, data, **kwargs):
        if data and 'email' in data and isinstance(data['email'], str):
            data['email'] = data['email'].strip().lower()
        return data