import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from attacks.single_key.dixon_attack import Dixon
from attacks.single_key.ecm_attack import ECMAttack
from attacks.single_key.low_public_key_attack import LowPublicKey
from attacks.single_key.pollard_rho_attack import PollardRho
from attacks.single_key.siqs_attack import SIQsieve


class Solution(AbstractAttack):
    def __init__(self):
        super().__init__("Solution")

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz):
        dixon = Dixon()
        d = dixon.attack(e, n)
        if not d == -1 :
            return d

        if n.bit_count() <= 71:
            rho = PollardRho()
            d = rho.attack(e, n)
            if not d == -1:
                return d

        elif n.bit_count() == 92 or n.bit_count() == 69 or 71 < n.bit_count() < 79:
            ecm = ECMAttack()
            d = ecm.attack(e, n)
            if not d == -1:
                return d

        else:
            siqs = SIQsieve()
            d = siqs.attack(e, n)
            if not d == -1:
                return d



