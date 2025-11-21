import gmpy2, attacks, lib.number_theory

from attacks.single_key.abstract_attack import AbstractAttack
from lib.number_theory import log, isqrt, primes, powmod, gcd, invert


def pollard_p_1(n:gmpy2.mpz):
    primelist = []
    logn = log(isqrt(n))  # 计算n的整数平方根的自然对数
    prime = primes(gmpy2.mpz(11451))  # 生成前11451个素数列表

    # 构造指数数组z
    for i in range(0, len(prime)):
        primei = prime[i]
        logp = log(primei)
        # 将素数primej重复足够次数，确保覆盖p-1的幂次
        primelist.extend(primei for _ in range(1, int(logn / logp) + 1))

    # 尝试每个小素数作为基a
    for a in prime:
        for i in range(0, len(primelist)):
            a = powmod(a, primelist[i], n)  # 逐步提升指数，模n
            p = gcd(n, a - 1)  # 计算GCD
            if n > p > 1:
                return p, n // p  # 找到因子，返回结果

    return -1


class PollardP_1(AbstractAttack):
    def __init__(self):
        super().__init__("PollardP1")


    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz):
        poll_re = pollard_p_1(n)
        if type(poll_re) == int:
            return -1
        if not(poll_re and len(poll_re) > 1):
            return -1

        p, q = poll_re
        phi = (p - 1) * (q - 1)
        return invert(e, phi)


if __name__ == "__main__":
    p = PollardP_1()
    print(p.attack(5, 35))
