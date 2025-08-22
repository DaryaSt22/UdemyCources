def validate_arg(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of the {arg} is {type(arg)}",
                                 "All arguments must be int or float !")
        #result = fn(*args, **kwargs)
        #return result
        return fn(*args, **kwargs)

    return wrapper


@validate_arg
def sum_nums(a, b):
    return a + b


try:
    print(sum_nums(4, 9))
    print(sum_nums(10.5, 11.6))
    print(sum_nums(10.5, '2.0'))
except ValueError as e:
    print(e)
