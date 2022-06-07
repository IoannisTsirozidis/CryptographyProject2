import random
import math
from timeit import default_timer as timer

# https://github.com/NikolaiT/Large-Primes-for-RSA/blob/master/generate_primes.py
# https://www.codespeedy.com/fast-exponentiation-python/

def miller_rabin_primality_test(p: object, s: object = 5) -> object:
    if p == 2:
        return True
    if not (p & 1):
        return False

    p1 = p - 1
    u = 0
    r = p1

    while r % 2 == 0:
        r >>= 1
        u += 1

    assert p - 1 == 2 ** u * r

    def witness(a):
        """
        Returns: True, if there is a witness that p is not prime.
                False, when p might be prime
        """
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = square_and_multiply(a, 2 ** i * r, p)
            if z == p1:
                return False
        return True

    for j in range(s):
        a = random.randrange(2, p - 2)
        if witness(a):
            return False

    return True


def square_and_multiply(x, k, p=None):
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r ** 2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r


if __name__ == "__main__":
    start = timer()
    p = 1068669447 * pow(2, 211088) -1

    if miller_rabin_primality_test(p):
        print("The number 1068669447* 2^211088 - 1 is prime!")
        print("Checking to see if q= 2*p+1 and p are safe primes...")
        q = 2 * p + 1
        if print(miller_rabin_primality_test(q)):
            print("q is also prime. p and q are safe primes.")

    else:
        print("p is not prime, so p and q are not safe primes.")



