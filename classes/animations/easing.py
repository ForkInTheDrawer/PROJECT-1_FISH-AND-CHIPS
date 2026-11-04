
# NOTE: t means time passed

def linear(t):
    return t


def ease_in(t):

    return t*t

def ease_out(t):
    return 1 - (1-t) **2

def ease_in_out(t):
    return 3 * t **2 - 2 *t **3