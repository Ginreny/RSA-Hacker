import timeit

from matplotlib import pyplot as plt
from tqdm import tqdm

from attacks.single_key.Fermat2 import Fermat2
from attacks.single_key.abstract_attack import AbstractAttack
from attacks.single_key.dixon_attack import Dixon
from attacks.single_key.ecm_attack import ECMAttack
from attacks.single_key.fermat1 import Fermat1
from attacks.single_key.pollard_rho_attack import PollardRho
from attacks.single_key.siqs_attack import SIQsieve
from generators.filemaker.RSAKeyGenerator import RSAKeyGenerator


class Tester:
    def __init__(self):
        pass

    def __test__(self, attack_method:AbstractAttack, keys:list):
        pass

    def test(self, test1, test2, test_range:list, test_time):
        t1_times = []
        t2_times = []
        keys = []

        bits_list = test_range
        for i in tqdm(bits_list):
            key_gen = RSAKeyGenerator(i)
            keys.clear()
            for _ in range(test_time):
                keys.append(key_gen.generateKeys())

            t1 = timeit.timeit(lambda: test1.test(keys), number=1)
            t2 = timeit.timeit(lambda: test2.test(keys), number=1)
            t1_times.append(t1)
            t2_times.append(t2)



        # print(f"rho平均耗时: {t1 / 100:.6f} 秒")
        # print(f"siqs平均耗时: {t2 / 100:.6f} 秒")

        # e1,n = key_gen.generateKeys()
        # print(e.attack(e1, n))

        plt.plot(bits_list, t1_times, label='RHO', color='black', linestyle='--')
        plt.plot(bits_list, t2_times, label='SIQS', color='gray', linestyle='-')
        plt.xticks(range(48,97, 4))
        plt.xlabel('Bit (bit)')
        plt.ylabel('Time (seconds)')
        plt.title('RSA Attack Performance')
        plt.legend()
        plt.grid(True)
        plt.savefig("RSA Attack Method Time Cost.svg", dpi=300)
        plt.show()

if __name__ == '__main__':
    test1 = PollardRho()
    test2 = SIQsieve()
    # test1.test([(5,35)])
    tester = Tester()
    tester.test(test1, test2, range(48,97), 10)

