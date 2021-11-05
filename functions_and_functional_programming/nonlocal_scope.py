message = 'global'

def enclosing():
    message = 'enclosing'

    def local():
        # global message
        nonlocal message
        message = 'local'

    #checking if message is affected

    print(f"enclosing message: {message}")
    local()
    print(f"enclosing message: {message}")


if __name__ == "__main__":

    # checking if global message gets affected

    print(f"global message: {message}")
    enclosing()
    print(f"global message: {message}")



