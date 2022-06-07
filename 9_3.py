import math
import random


def primefactors(n):
    factors = []
    count_factors = []
    k=1
    # even number divisible
    while n % 2 == 0:
        if 2 in factors:
            k+=1
            n = n / 2
        else:
            factors.append(2)
            n = n / 2

    count_factors.append(k)


    # n became odd
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        k = 1
        while n % i == 0:
            if i in factors:
                k+=1
                n = n /i
            else:
                factors.append(i)
                n = n / i

        count_factors.append(k)

    k=1
    if n > 2:
        factors.append(n)
        count_factors.append(k)

    return factors, count_factors


def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num % n==0:
            return False
    return True




# IMPORTANT NOTICE: The following program can accept integers with a maximum of 263, to avoid Result-Overflowing


if __name__ == "__main__":


    p = int(input("Enter a prime number, in the spectrum [3, 263]: "))
    while not isprime(p) or p<=2 or p>263:
        print("Wrong input")
        p = int(input("Enter a prime number, greater than 2: "))


    factors, count_factors = primefactors(p-1)

    print("prime factorization:  ")
    for i in range(len(factors)):
        print(factors[i], ' (',count_factors[i],'), ')
    print()


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







