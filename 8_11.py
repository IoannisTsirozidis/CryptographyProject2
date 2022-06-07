# AMICABLE NUMBERS

# Amicable numbers; we call numbers m and n to be amicable if:
# sum(proper_divisors(m)) == n    AND    sum(proper_divisors(n)) == m


# *A proper divisor of a natural number is the divisor that is strictly less than the number.
# For example, number 20 has 5 proper divisors: 1, 2, 4, 5, 10*
import time

def proper_divisors(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)

    return div


def amicable_numbers(m, n):
    if sum(proper_divisors(m)) == n and sum(proper_divisors(n)) == m:
        return True
    else:
        return False


if __name__ == "__main__":

    start_time = time.time()
    print("proper divisors of 220: ", proper_divisors(220))
    print("proper divisors of 284: ", proper_divisors(284))

    #increase the first number by one so the search for the next couple of numbers won't include the first one.
    m = 221
    n = 284

    flag = 0
    for i in range(222, 2000):
        for j in range(284, 2000):
            #print(i, j)
            if i != j and amicable_numbers(i, j) is True:
                #print(i, j)
                m=i
                n=j
                flag =1
                break

        if flag ==1:
            break


    print(m, n)
    print("--- %s seconds ---" % (time.time() - start_time))