import math
from timeit import default_timer as timer



#I defined the positive divisors to be all numbers i between [1,m] that satisfy: m % i ==0 , i ε [1, m]
def sum_of_positive_divisors(m):

    positive_divisors = []
    for i in range(1, m+1):
        if m % i ==0:
            positive_divisors.append(i)

    return sum(positive_divisors)





if __name__ == "__main__":

    start = timer()
    gama = 0.57721566490153286060651209008240243104
    e = math.e
    limit = pow(10, 5)
    maxi = 0
    egama = pow(e, gama)

    for i in range(2, limit):
        if sum_of_positive_divisors(i)> egama * i * math.log(math.log(i, e), e):
            maxi = i

    end = timer()

    print("final result: ", maxi)
    print("Time elapsed in sec: ", end - start)

