import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import is_square, isqrt, invert


def fermat1(n:gmpy2.mpz):
    if (n - 2) & 3 == 0: # n % 4 == 2
        return -1

    y = 1
    while not is_square(n + gmpy2.square(y)):
        y += 1

    x = isqrt(n + gmpy2.square(y))
    return x- y, x + y

class Fermat1(AbstractAttack):
    def __init__(self):
        super().__init__("Fermat1")

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz):
        p, q = fermat1(n)
        phi = (p - 1) * (q - 1)
        if phi == 0:
            return -1
        return invert(e, phi)

if __name__ == "__main__":
    f = Fermat1()
    print(f.attack(5, 35))