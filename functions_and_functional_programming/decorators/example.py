from utils_decorators import escape_unicode, CallCount


@escape_unicode
def northern_city():
    return 'Tromsø'

@CallCount
def hello(name):
    print(f"Hello, {name}")


