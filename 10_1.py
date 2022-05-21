import math
def trial_division_factorization(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    f = 3

    while f**2 <= n:
        if n % f == 0:
            factors.append(f)
            n = n / f
        else:
            f = f + 2


    if n != 1:
        factors.append(n)

    return factors



def isprime(n):
    for i in range(2, math.ceil(n**0.5)):
        if n % i == 0:
            return False

    return True



# Driver code
if __name__ == "__main__":


    print('factorizing 2^62-1: ', trial_division_factorization(2**62-1))
    print('factorizing 2^102-1: ', trial_division_factorization(2**102-1))
