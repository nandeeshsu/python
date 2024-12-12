# python-tutorial

create python virtual environment

    python3 -m venv .venv

Activate the created virtual environment

    source .venv/bin/activate

After activating the virtual environment install all the dependencies using pip and requirements.txt

    pip3 install -r requirements.txt

Using python dependency manager instead of requirements.txt. It's similar to NPM in nodejs. Below command will create the virtual environment. First we have to install this dependency manager via pip3 install pipenv

    pipenv --python 3.10.9

Install dependency like flask for example. This will install local to the project not globally

    pipenv install flask 2.3.2

curl command for POST

curl --location --request POST 'http://localhost:5000/api/v1/incomes' \
--header 'Content-Type: application/json' \
--data-raw '{
  "description": "lottery",
  "amount": 1000.0
}'


# some concepts
    unpacking operator *, **
    non-defualt arguments should preceed defualt arguments
    *args should come before **kwargs

    To recap, the correct order for your parameters is:

        Standard arguments
        *args arguments
        **kwargs arguments

    *args = tuple
    *kwagrs = dict