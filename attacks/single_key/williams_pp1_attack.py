import gmpy2, attacks, lib.number_theory
import primefac

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import isqrt, ilogb, mlucas, gcd, next_prime, invert


def williams_p1(n:gmpy2.mpz):
    prime, n_sqrt = 2, isqrt(n)

    while True:
        v = 1
        while True:
            max_exp = ilogb(n_sqrt, prime)
            if max_exp == 0: break

            for _ in range(max_exp):
                v = mlucas(v, prime, n)

            p = gcd(v - 2, n)
            if 1 < p < n: return p, n // p
            if p == n: break

            prime = next_prime(prime)


class WilliamsPP1(AbstractAttack):
    def __init__(self):
        super().__init__("WilliamsPP1")

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz):
        p = primefac.williams_pp1(n)
        q = n // p
        phi = (p - 1) * (q - 1)
        return invert(e, phi)

if __name__ == "__main__":
    w = WilliamsPP1()
    print(w.attack(5, 35))
