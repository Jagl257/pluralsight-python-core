from functools import wraps


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

class CallCount:

    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

def noop(f):
    def noop_wrapper():
        return f()
    return noop_wrapper

def noop_with_same_f_values(f):
    def noop_wrapper():
        return f()

    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper

def noop_with_wraps(f):
    @wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper

def check_non_negative(index):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if args[index] < 0:
                raise ValueError(f"Argument {index} must be non-negative")
            return f(*args, **kwargs)
        return wrapper
    return decorator



