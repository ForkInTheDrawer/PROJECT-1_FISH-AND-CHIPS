
# NOTE: t means time passed

def linear(t):
    return t


def ease_in(t):

    return t*t

def ease_out(t):
    return 1 - (1-t) **2

def ease_in_out(t):
    return 3 * t **2 - 2 *t **3

def ease_out_back(t):
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * (t - 1)**3 + c1 * (t - 1)**2