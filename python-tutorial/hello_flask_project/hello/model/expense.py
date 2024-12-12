from marshmallow import post_load

from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

class Expense(Transaction):
    # The __init__ method is the Python equivalent of the constructor in an object-oriented approach
    # The __init__ function is called every time an object is created from a class. 
    # The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes
    def __init__(self, description, amount):
        super(Expense, self).__init__(description, -abs(amount), TransactionType.EXPENSE)

    # The __repr__() method returns a more information-rich, or official, string representation of an object. 
    # In general, the __str__() string is intended for users and the __repr__() string is intended for developers.
    # The __str__() method returns a human-readable, or informal, string representation of an object
    def __repr__(self):
        return '<Expense(name={self.description!r})>'.format(self=self)
    
class ExpenseSchema(TransactionSchema):
    @post_load
    def make_expense(self, data, **kwargs):
        return Expense(**data)