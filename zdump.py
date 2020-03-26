#!/usr/bin/python3
def dump(func):
    def wrapped(*args, **kwargs):
        print("Function: \t{}".format(func.__name__))
        print("Input args: \t{}".format(''.join((map(str, args)))))
        print("Input keywaordd args: \t{}".format(kwargs.items()))
        output = func(*args, **kwargs)
        print("Output: \t{}".format(output))
        return output
    return wrapped