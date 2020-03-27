def cuber(a):
    result = a * a
    return result


def step_counter(distance, step_length):
    numb_of_steps = distance / step_length
    return numb_of_steps


def absolute_difference(a, b):
    if a > b:
        return a - b
    else:
        return b - a
