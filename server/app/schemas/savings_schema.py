from extensions import ma
from models.savings import Savings

class SavingsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Savings
        load_instance = True
        include_fk = True
        unknown = ma.EXCLUDE

saving_schema = SavingsSchema()
savings_schema = SavingsSchema(many=True)