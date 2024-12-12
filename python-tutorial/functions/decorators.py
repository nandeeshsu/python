import functools
import time

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

# Technical Detail: The @functools.wraps decorator uses the function functools.update_wrapper() to update special attributes 
# like __name__ and __doc__ that are used in the introspection.

def do_twice1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

# boilerplate template for the decorator
def decorator(func):
    @functools.wraps(func)
    def wrapped_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value
    return wrapped_decorator


def timer(func):
    """Prints the execution time of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwars):
        start_time = time.perf_counter()

        value = func(*args, **kwars)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(f"Finished execution of function {func.__name__!r} in {execution_time:.4f} seconds")

        return value
    return wrapper_timer

def debug(func):
    """Prints the function signature and the return value """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(i) for i in args]

        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]

        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__} returned {value!r}")
        return value
    return wrapper_debug
