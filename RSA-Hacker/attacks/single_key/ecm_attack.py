import primefac
import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import invert


class ECMAttack(AbstractAttack):
    def __init__(self):
        super().__init__("ECMAttack")

    def attack(self, e: gmpy2.mpz, n: gmpy2.mpz):
        p = primefac.ecm(n)
        q = n // p
        phi = (p - 1) * (q - 1)
        return invert(e, phi)


if __name__ == "__main__":
    pass