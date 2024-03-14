def add(num_one, num_two):
    return num_one + num_two


def div(num_one, num_two):

    if num_two == 0:
        raise ValueError
    return num_one/num_two

