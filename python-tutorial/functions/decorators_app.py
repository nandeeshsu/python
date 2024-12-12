# https://realpython.com/primer-on-python-decorators/

#  Decorators
from decorators import do_twice
from decorators import do_twice1
from decorators import timer
from decorators import debug
import math
import random

#  Simple decorators
def my_decorator(func):
    def wrapper():
        print("wrapper start")
        func()
        print("wrapper end")
    return wrapper

def say_hi():
    print("Hi, Decorator")

say_hi = my_decorator(say_hi)

print(say_hi)
print(say_hi())
print("***********************************")
@my_decorator
def say_hi_twice():
    print("Hi Once")
    print("Hi Twice")

say_hi_twice()

print("----------------------------------------")



def convert_upper(f):
    print("Inside convert_upper function")

    def wrap(*args, **kwargs):
        print("inside wrap function")

        x = f(*args, **kwargs)
        return x.upper()
    return wrap

@convert_upper
def print_upper(name):
    print("Inside print_upper function")
    return name

print("Converted to upper case ==> ", print_upper("work, 1=mita, 2=nandeesh, test"))

# print("Converted to upper case ==> ", print_upper(["test", "test1"]))

@do_twice
def say_hello():
    print("Hello")

say_hello()

# decorating function with arguments
@do_twice
def say_hello(name):
    print(f"hello {name}")

say_hello("mita")

# returning values from decorated function

@do_twice
def return_greeting(name):
    print("inside return_greeting function")
    return f"hello {name}"

# this prints None rather than Priya
print(return_greeting("Priya"))

return_greeting = return_greeting("Priya")
print(return_greeting)

#  who you really are

print(say_hello)

# this prints decorators wrapped function name "wrapper"
print(say_hello.__name__)

@do_twice1
def say_hello1():
    print("Hello1")

print(say_hello1)
# this prints the original name of function which is "say_hello1". This is achieved using "@functool.wrap" decorator
print(say_hello1.__name__)

# The @timer decorator is great if you just want to get an idea about the runtime of your functions. 
# If you want to do more precise measurements of code, you should instead consider the timeit module in the standard library. 
# It temporarily disables garbage collection and runs multiple trials to strip out noise from quick function calls.
@timer
def takes_long_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

takes_long_time(999)

@debug
def do_greetings(name, age=None):
    if age is None:
        return f"how are you {name}"
    else:
        return f"{name}, {age} already growing up "
    
print(do_greetings("Mita", 8))
print(do_greetings("Mita"))

# apply decorator to a function that has already been defiend 

# apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum( 1 / math.factorial(n) for n in range(terms))

approximate_e(5)

# registering plugins

PLIGINS = dict()

def register(func):
    """Register a function as a plugin"""
    PLIGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello, {name}"

@register
def say_hi(name):
    return f"Hi, {name}"

# The @register decorator simply stores a reference to the decorated function in the global PLUGINS dict. 
# Note that you do not have to write an inner function or use @functools.wraps in this example because 
# you are returning the original function unmodified
def greet_randomly(name):
    greeter_key, greeter_func = random.choice(list(PLIGINS.items()))
    print(f"using function {greeter_key!r}")
    print(greeter_func(name))

greet_randomly("Mita")