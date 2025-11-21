import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import isqrt_rem, is_square, isqrt, invert


def fermat2(n:gmpy2.mpz):
    if (n - 2) & 3 == 0:
        return -1

    x, r = isqrt_rem(n)
    y_square = -r
    it = (x << 1) + 1

    while not is_square(y_square):
        y_square += it
        it += 2

    x = (it - 1) >> 1
    y = isqrt(y_square)
    return x - y, x + y

class Fermat2(AbstractAttack):
    def __init__(self):
        super().__init__("Fermat2")

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz ):
        p, q = fermat2(n)
        phi = (p - 1) * (q - 1)
        return invert(e, phi)


if __name__ == "__main__":
    f = Fermat2()
    print(f.attack(5, 35))