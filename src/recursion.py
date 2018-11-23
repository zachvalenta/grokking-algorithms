def countdown(arg):
    print(arg)
    return None if arg == 0 else countdown(arg - 1)


def do_sum(arg):
    if arg == 0:
        return arg
    else:
        return arg + do_sum(arg - 1)


def do_factorial(arg):
    if arg == 1:
        return arg
    else:
        return arg * do_sum(arg - 1)
