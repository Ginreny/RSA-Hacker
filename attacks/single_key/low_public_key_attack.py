import gmpy2, attacks, lib.number_theory

from attacks.multi_key.abstract_attack import AbstractAttack


class LowPublicKey(AbstractAttack):
    def __init__(self):
        super().__init__("LowPublicKey")

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz, c:gmpy2.mpz):
        if e > 5: return -1

        for k in range(1, n):
            m_tmp = gmpy2.iroot(c + k * n, e)[0]
            if gmpy2.powmod(m_tmp, e, n) == c:
                return m_tmp

