import gmpy2

# https://wiremask.eu/articles/fermats-prime-numbers-factorization/
# the only point in the code where gmpy2 is used.
# Wiremask provided a really elegant and time-efficient method here.

def fermat_factor(n):
    assert n % 2 != 0

    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n

    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n

    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)

    return int(p), int(q)



def mod_inv(e, phi):
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


# https://github.com/drazioti/book_crypto
# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
# Slight modification of the code. Implemented changes based on drazioti's crypto_text_book

def mod_power(base, exponent, m):
    result = 1
    base = base % m
    if base == 0:
        return 0

    while exponent > 0:
        # Case where y is even.
        if (exponent & 1) == 1:
            result = (result * base) % m
        # y must be even now
        exponent = exponent >> 1  # y = y/2
        base = (base * base) % m
    return result



# A few points of notice for RSA:

#       N can be factorized to the primes p and q
#       phi(N) can be found via:  phi(N) = (p-1)*(q-1)

#       c = m^e mod N (encryption)
#       m = c^d mod N (decryption)


if __name__ == "__main__":

    C = [3203, 909, 3143, 5255, 5343,
         3203, 909, 9958, 5278, 5343,
         9958, 5278, 4674, 909, 9958,
         792, 909, 4132, 3143, 9958,
         3203, 5343, 792, 3143, 4443]

    N = 11413
    e = 19

    p, q = fermat_factor(11413)

    # p = 101
    # q = 113

    phi = (p - 1) * (q - 1)


    d = mod_inv(e, phi)
    d = d % phi
    s = ''

    for i in C:
        dec = mod_power(i, d, N)
        s += chr(dec)

    print(s)


    # e: 1    ಃ΍ేᒇᓟಃ΍⛦ᒞᓟ⛦ᒞቂ΍⛦̘΍ဤే⛦ಃᓟ̘ేᅛ
    # e: 3    ḻ௖ⱺ⣘ᶡḻ௖ᩃᘆᶡᩃᘆ੹௖ᩃǅ௖∁ⱺᩃḻᶡǅⱺǸ
    # e: 9    ᷉≓Ⲓᄿᐕ᷉≓ྨᘍᐕྨᘍؕ≓ྨ⏂≓᱇Ⲓྨ᷉ᐕ⏂Ⲓ᫓
    # e: 11   ⱒ˃Ÿ▥މⱒ˃⋡ʄމ⋡ʄ࿊˃⋡௬˃⠏Ÿ⋡ⱒމ௬Ÿᓨ
    # e: 13   ᙢᒄ஋᩺ԗᙢᒄśếԗśế޾ᒄś⛙ᒄ╧஋śᙢԗ⛙஋ܙ
    # e: 17    ᗣṡῪఠ໴ᗣṡᗚ৛໴ᗚ৛ڒṡᗚ὘ṡ␶Ὺᗚᗣ໴὘ῪⰯ
    # e: 19    welcowe to the real world
