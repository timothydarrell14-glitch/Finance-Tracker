from extensions import ma
from models.transactions import Transactions

class TransactionsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transactions
        load_instance = True
        include_fk = True
        unknown = ma.EXCLUDE

transaction_schema = TransactionsSchema()
transactions_schema = TransactionsSchema(many=True)