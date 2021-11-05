# Testing local funtions and their scope:

def function_1():
    def inner_function():
        print("Hello I am an inner funtion")
    inner_function()

def function_2():
    def inner_function(a, b):
        print(f"{a} + {b} = {a+b}")
    return inner_function

def enclosing():
    x = 'closed over'
