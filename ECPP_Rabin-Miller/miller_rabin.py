"""
Implementation of Miller-Rabin test.
"""
import random


def miller_rabin(n, k):
    """
    Main method
    Args:
        n:
        k: number of loops (randomly choosing witnesses)

    Returns:
        Miller-Rabin witness or False.
    """
    for i in range(0, k):
        a = random.randrange(2, n - 1)
        if not miller_rabin_once(n, a):
            return a
    return False


def miller_rabin_once(n, a):
    """
    Single Witness loop.
    Args:
        n:
        a:

    Returns:
        True if n is probable prime, False if it is composite.
    """
    if n % 2 == 0:
        return False
    e, k = decompose(n - 1)

    a = pow(a, k, n)
    if a == 1:
        return True
    for i in range(0, e):
        if a == -1 % n:
            return True
        a = pow(a, 2, n)
    return False


def decompose(n):  # decomposes n into 2^e * k
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e, n


def explain(x):
    if not x:
        print 'composite'
    else:
        print 'probable prime'


if __name__ == '__main__':
    explain(miller_rabin(838041647, 20))
