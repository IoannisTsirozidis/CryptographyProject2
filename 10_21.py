import random
import math

#
# # Pollard Rho is an integer factorization algorithm, which is quite fast for large numbers.
# # It is based on Floyd’s cycle-finding algorithm and on the observation that two numbers x and y are
# # congruent modulo p with probability 0.5 after 1.177\sqrt{p} numbers have been randomly chosen.
# This version of the code is a fully optimized and modified version of the code to be found here:
# #https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/


# Find a prime factor of composite
def pollardFactorization(N):
    if N % 2 == 0:
        return 2
    x = random.randint(1, N - 1)  # random selection between 1, n-1
    y = x
    c = random.randint(1, N - 1)
    g = 1
    while g == 1:
        x = ((x * x) % N + c) % N
        y = ((y * y) % N + c) % N    # a series of modular steps known as
        y = ((y * y) % N + c) % N    # hare and tortoise moves.
        g = math.gcd(abs(x - y), N)  # checks for

    return g



# Driver function
if __name__ == "__main__":
    n = pow(2,25) - 1

    print('A prime divisor for the given number n: ', n, '\n is: ', pollardFactorization(n))

