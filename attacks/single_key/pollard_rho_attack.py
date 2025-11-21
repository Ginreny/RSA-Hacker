import primefac.primefac
import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import powmod, gcd, invert


def pollard_rho(n:gmpy2.mpz):
    p = gmpy2.mpz(1),
    x = gmpy2.mpz(2),
    y = gmpy2.mpz(2),
    g = lambda x: powmod(x, 2, n) + 1

    while p == 1:
        x = g(x)
        y = g(g(y))
        p = gcd(abs(y - x), n)

    return p

class PollardRho(AbstractAttack):
    def __init__(self):
        super().__init__("PollardRho")

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz):
        p = primefac.pollardrho_brent(n)
        q = n // p
        phi = (p - 1) * (q - 1)
        if phi != 0:
            return invert(e, phi)
        return -1

if __name__ == "__main__":
    p = PollardRho()
    print(p.attack(gmpy2.mpz(5), gmpy2.mpz(35)))

