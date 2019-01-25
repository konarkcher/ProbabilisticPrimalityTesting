from math import sqrt
import time


def trial_division(n, timer=0):
    """
    Trial division algorithm
    Args:
        n: Probable Prime

    Returns:
        If n is prime
    """
    start = time.time()
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        if timer > 0:
            if time.time() - start > timer:
                return 'too long'
    return True
