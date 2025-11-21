import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import log, isqrt, primes, powmod, gcd, invert


def pollard_p_1(n:gmpy2.mpz):
    primelist = []
    logn = log(isqrt(n))  # Calculate natural logarithm of integer square root of n
    prime = primes(gmpy2.mpz(11451))  # Generate list of first 11451 primes

    # Construct exponent array z
    for i in range(0, len(prime)):
        primei = prime[i]
        logp = log(primei)
        # Repeat prime primej enough times to cover powers of p-1
        primelist.extend(primei for _ in range(1, int(logn / logp) + 1))

    # Try each small prime as base a
    for a in prime:
        for i in range(0, len(primelist)):
            a = powmod(a, primelist[i], n)  # Gradually increase exponent, modulo n
            p = gcd(n, a - 1)  # Calculate GCD
            if n > p > 1:
                return p, n // p  # Found factor, return result

    return -1


class PollardP_1(AbstractAttack):
    def __init__(self):
        super().__init__("PollardP1")


    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz):
        poll_re = pollard_p_1(n)
        if type(poll_re) == int:
            return -1
        if not(poll_re and len(poll_re) > 1):
            return -1

        p, q = poll_re
        phi = (p - 1) * (q - 1)
        return invert(e, phi)


if __name__ == "__main__":
    p = PollardP_1()
    print(p.attack(5, 35))
