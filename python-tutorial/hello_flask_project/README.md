# Tutorial Referred
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/


pipenv is used as dependency manager. 

# To install the pipenv

    pip install pipenv

# To create python virtual environment for a project. Run it under the project folder. --three is for python3. This will created 2 files, Pipfile and Pipfile.lock. Pipfile will contains details like python version and the packages/libraries needed. Pipfile.lock will contain the precise version of the direct dependencies and transitive dependencies.

    pipenv --three

# To install a dependency using the dependency manager pipenv. For example for the flask

    pipenv install flask

# Marshmallow is used for converting complex datatypes such as objects to and from built-in python data types. Also can be used to validate, serialize and deserialize data

# get expenses
curl http://localhost:5000/api/v1/expenses

# add a new expense
curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 20,
    "description": "lottery ticket"
}' http://localhost:5000/api/v1/expenses

# get incomes
curl http://localhost:5000/ap1/v1/incomes

# add a new income
curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 300.0,
    "description": "loan payment"
}' http://localhost:5000/api/v1/incomes

# build the image
docker build -t hello-flask-project .

# run a new docker container named cashman
docker run --name hello-flask-project \
    -d -p 5000:5000 \
    hello-flask-project

# fetch incomes from the dockerized instance
curl http://localhost:5000/api/v1/incomes/

# Using Docker Compose
    docker-compose build
    docker-compose up -d
    docker-compose down -v

    http://localhost:1337/api/v1/expenses