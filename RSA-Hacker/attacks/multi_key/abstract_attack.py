import gmpy2


class AbstractAttack:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def attack(self, e:gmpy2.mpz, n:gmpy2.mpz):
        pass

    def test(self, keys):
        for i in keys:
            e, n = i
            self.attack(e, n)
