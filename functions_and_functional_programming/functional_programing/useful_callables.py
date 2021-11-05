from itertools import count

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)
        return wrap


def numbering_elements(elements: list):
    return map(lambda x,y: (x,y), count(), elements)
