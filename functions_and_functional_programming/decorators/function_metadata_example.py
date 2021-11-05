from utils_decorators import noop, noop_with_same_f_values, noop_with_wraps

@noop
def hello():
    "Prints a well known message"
    print("Hello World")


@noop_with_same_f_values
def hello_2():
    "This also prints a well known message"
    print("Hello World")

@noop_with_wraps
def hello_3():
    "This will do the same as the others"
    print("Hello World")


if __name__=="__main__":
    
    hello()
    print(hello.__name__)
    print(hello.__doc__)

    print("----------------")

    hello_2()
    print(hello_2.__name__)
    print(hello_2.__doc__)

    print("----------------")

    hello_3()
    print(hello_3.__name__)
    print(hello_3.__doc__)




