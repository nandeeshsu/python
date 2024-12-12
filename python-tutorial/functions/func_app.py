def increment_by_one(number):
    print("increment_by_one function called")
    return number + 1

print(increment_by_one(2))

# functions are first class objects, meaning functions can be passed and used as arguments just like any other objects

def say_hello(name):
    return f"Hello {name}"

print(say_hello("Mita"))

def be_nice(name):
    return f"Hi {name} be nice"

print(be_nice("Mita"))

# passing function as argument to another function
def greet_mita(greeter_func):
    return greeter_func("Mita")

print(greet_mita(say_hello))
print(greet_mita(be_nice))

# Inner functions, locally scoped to parent. If we directly call the inner/child function should get error.

def parent_function():
    print("From parent function")

    def first_inner_function():
        print("From first inner/child function")
    def sencond_inner_function():
        print("From second inner/child function")

    sencond_inner_function()
    first_inner_function()

parent_function()

