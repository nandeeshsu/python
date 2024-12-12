# run using the command flask --app helloApi run

from flask import Flask, request
import functools

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to Hello, World API !!!"

def login_required(func):
    """
    Make sure user is logged in before proceeding
    """
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if 'Authorization' in request.headers:
            authHeader = request.headers['Authorization']
        else:
            return "login failure"
        return func(*args, **kwargs)
    return wrapper_login_required
        
@app.route("/secret")
@login_required
def secrets():
    return "Success"