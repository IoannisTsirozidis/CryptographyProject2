# This is a Modified version of Nikolai Tschacher's code
# https://github.com/NikolaiT
# https://github.com/NikolaiT/Large-Primes-for-RSA/blob/master/generate_primes.py


import random

#INDEPENDENT
def fermat_primality_test(p, s=5):

    if p == 2:
        return True
    if not p & 1: # if p is even, number cant be a prime
        return False

    for i in range(s):
        a = random.randrange(2, p-2)
        x = pow(a, p-1, p) # a**(p-1) % p
        if x != 1:
            return False
    return True


#INDEPENDENT
def square_and_multiply(x, k, p=None):

    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r = r**2
        if i == '1':
            r = r * x
        if p:
            r %= p
    return r


#SUBFUNCTION witness.
def miller_rabin_primality_test(p, s=5):
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

    assert p-1 == 2**u * r

    def witness(a):
        """
        Returns: True, if there is a witness that p is not prime.
                False, when p might be prime
        """
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = square_and_multiply(a, 2**i * r, p)
            if z == p1:
                return False
        return True

    for j in range(s):
        a = random.randrange(2, p-2)
        if witness(a):
            return False

    return True



def generate_primes(n=512, k=1):

    assert k > 0
    assert n > 0 and n < 4096

    x = random.getrandbits(n)

    primes = []

    while k>0:
        if miller_rabin_primality_test(x, s=7):
            primes.append(x)
            k = k-1
        x = x+1

    return primes


if __name__ == '__main__':
    n = 1024

    primes = generate_primes(n=n)
    print(primes[0])
    while not miller_rabin_primality_test(2*primes[0]+1,4):
        primes = generate_primes(n)
        print(primes[0])




    print("final result:")
    print("p: ", primes[0])
    print("q=2p+1: ", 2*primes[0]+1)



