import math
import random


def primefactors(n):
    factors = []
    # even number divisible
    while n % 2 == 0:
        factors.append(2),
        n = n / 2

    # n became odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i

    if n > 2:
        factors.append(n)

    return factors


def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True







if __name__ == "__main__":


    p = int(input("Enter a prime number, greater than 2: "))
    while not isprime(p) or p<=2:
        print("Wrong input")
        p = int(input("Enter a prime number, greater than 2: "))


    factors = primefactors(p-1)
    print("prime factorization:  ", factors)

    a_choices = [i for i in range(2, p-1)]
    print("values from [2, p-2]: ", a_choices)



    random_a = random.choice(a_choices)
    flag = 0
    while flag == 0:
        for i in factors:
            if (random_a ** ((p-1)/i) ) % p == 1:
                flag = 1

        if flag == 0:
            break
        else:
            flag = 0
            random_a = random.choice(a_choices)

    print()
    print()
    print("result: ", random_a)







