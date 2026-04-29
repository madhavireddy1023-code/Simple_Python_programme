# Basic Decorator Example
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with Arguments
def repeat(num_times):
    def decorators(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorators

@repeat(1)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# Decorator for Timing a Function
import time
from unittest import result

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def long_running_function():
    time.sleep(2)
    print("Finished long running function.")

long_running_function()

# Decorator for Caching Results
def cache(func):
    def wrapper(*args):
        if args in wrapper.cache:
            return wrapper.cache[args]
        result = func(*args)
        wrapper.cache[args] = result
        return result
    wrapper.cache = {}
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(30))

# Decorator for function name and arguments
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        args = list(args)
        if args:
            if len(args) > 1 and args[0] < args[1]:
                args[0], args[1] = args[1], args[0]          
        if kwargs:
            if 'a' in kwargs and 'b' in kwargs and kwargs['a'] < kwargs['b']:
                kwargs['a'], kwargs['b'] = kwargs['b'], kwargs['a']
        
        args = tuple(args)
        result = func(*args, **kwargs)
        return result
    return wrapper

@log
def add(a, b):
    return a/b
print(add(5, 10))

