import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import isqrt


class BruteForce(AbstractAttack):
    def __init__(self):
        super(BruteForce, self).__init__("BruteForce")
    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz):
        sqrt_n = isqrt(n)
        for i in range(sqrt_n):
            p = sqrt_n // i
            if p * i == n:
                return i
