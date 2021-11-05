"Exercise to understand the usage of multiple args functions"


def hypervolume_explained(*args):

    #this are the args
    print(args)
    #this is the type of args
    print(type(args))

def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)

    for length  in i:
        v *= length

    return v

def hypervolume_TypeError(length, *lengths):
    v = length

    for item in lengths:
        v *= item

    return v

def kw_hypervolume(**kwargs):

    #this are the kwargs
    print(kwargs)

    #this is the type of kwargs
    print(type(kwargs))

def tag(name, **attributes):

    result = '<' + name

    for key, value in attributes.items():
        result += f'{key}= "{str(value)}""'
    result += '>'
    return result
