from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from hello.model.expense import Expense, ExpenseSchema
from hello.model.income import Income, IncomeSchema
from hello.model.transaction_type import TransactionType

# from hello.requires_auth import requires_auth

app = Flask(__name__)

# incomes = [
#     { 'description': 'salary',
#       'amount': 50000
#     }
# ]

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('Pizza', 50),
    Expense('Rock Concert', 100)
]

@app.route("/")
def hello_world():
    return "Welcome to Hello, World Flask project!!!"

@app.route("/api/v1/incomes")
def get_incomes():
    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )
    return jsonify(incomes)

@app.route("/api/v1/incomes", methods=['POST'])
def add_incomes():
    # incomes.append(request.get_json())
    income = IncomeSchema().load(request.get_json())
    transactions.append(income)
    return '', 204

@app.route("/api/v1/expenses")
def get_expenses():
    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )
    return jsonify(expenses)

@app.route("/api/v1/expenses", methods=['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    transactions.append(expense)
    return "", 204

# This doesn't need authentication
@app.route("/ping")
@cross_origin(headers=['Content-Type', 'Authorization'])
def ping():
    return "All good. You don't need to be authenticated to call this"

# This does need authentication
@app.route("/secured/ping")
@cross_origin(headers=['Content-Type', 'Authorization'])
# @requires_auth
def secured_ping():
    return "All good. You only get this message if you're authenticated"

# if __name__ == "__main__":
#     app.run()