from math import sqrt


def trial_division(n):
    """
    Trial division algorithm
    Args:
        n: Probable Prime

    Returns:
        If n is prime
    """
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
