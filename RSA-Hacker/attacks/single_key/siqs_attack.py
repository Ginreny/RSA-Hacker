import primefac
import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import invert


class SIQsieve(AbstractAttack):
    def __init__(self):
        super().__init__("SIQsieve")

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz ):
        p = primefac.siqs(n)
        q = n // p
        phi = (p - 1) * (q - 1)
        return invert(e, phi)

def attack(e:gmpy2.mpz, n:gmpy2.mpz ):
    p = primefac.siqs(n)
    q = n // p
    phi = (p - 1) * (q - 1)
    return invert(e, phi)