import random
import bitarray

import gmpy2, attacks, lib.number_theory
from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import primes, powmod_base_list, isqrt, powmod, gcd, invert


def dixon_rand(n:gmpy2.mpz, B = 100, max_attempts = 10000):
    base_primes = primes(B)
    upper_square = pow(base_primes[-1], 2) + 5
    bukkit = bitarray.bitarray(upper_square) # Similar to bucket in bucket sort

    base_square = powmod_base_list(base_primes, 2, n)
    for p in base_square:
        bukkit[p] = 1

    nsqrt = isqrt(n)
    for _ in range(max_attempts):
        i = random.randint(nsqrt, n)
        i_square = powmod(i, 2, n)
        if i_square < upper_square and bukkit[i_square] == 1:
            for k in range(0, B):
                if 1 < (p := gcd(i - base_primes[k], n)) < n:
                    return p, n // p

    return -1, -1


class Dixon(AbstractAttack):
    def __init__(self):
        super().__init__("Dixon")

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz ):
        p,q = dixon_rand(n)
        if p == -1 or q == -1:
            return -1

        phi = (p - 1) * (q - 1)
        return invert(e, phi)

if __name__ == "__main__":
    d = Dixon()
    print(d.attack(5, 35))
