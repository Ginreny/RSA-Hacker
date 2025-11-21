import gmpy2, attacks, lib.number_theory
from attacks.single_key.abstract_attack import AbstractAttack
from attacks.single_key.factordb_connector import FactorDB
from lib.number_theory import invert


class Factordb(AbstractAttack):
    def __init__(self):
        super().__init__("Factordb")

    def attack(self, e, n):
        f = FactorDB(n)
        f.connect()
        p, q = f.get_factor_list()


        if p == n:
            return -1

        if p * q  != n:
            return -1

        phi = (p - 1) * (q - 1)
        return invert(e, phi)


if __name__ == "__main__":
    p = Factordb()
    print(p.attack(5, 35))
