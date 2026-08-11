from extensions import ma
from models.users import Users

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

    email = ma.Email(required=True, load_only=True)
    password = ma.String(required=True, load_only=True)