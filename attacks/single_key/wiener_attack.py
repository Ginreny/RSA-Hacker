import gmpy2, attacks, lib.number_theory
from attacks.single_key.abstract_attack import AbstractAttack
from typing import List, Tuple

def ration_to_confrac(x: gmpy2.mpz, y: gmpy2.mpz) -> Tuple[List[int], List[Tuple[int, int]]]:
    init_value = x // y

    confrac_list = [init_value]
    conver_list = [(init_value, gmpy2.mpz(1))]

    doule_pre_num, double_pre_de = gmpy2.mpz(1), gmpy2.mpz(0)  # Previous-previous numerator and denominator
    pre_num, pre_de = init_value, gmpy2.mpz(1)  # Previous numerator and denominator

    factor = init_value

    while factor * y != x:
        # Calculate current fraction coefficient
        x, y = y, x - factor * y
        factor = x // y
        confrac_list.append(factor)

        # Calculate current fraction value
        current_num, current_de = (
            factor * pre_num + doule_pre_num, factor * pre_de + double_pre_de)
        conver_list.append((current_num, current_de))

        # Iterate current fraction coefficient
        doule_pre_num, double_pre_de = pre_num, pre_de
        pre_num, pre_de = current_num, current_de

    # Break from loop when calculation is complete
    return confrac_list, conver_list


class Wiener(AbstractAttack):
    def __init__(self):
        super().__init__("Wiener")

    def attack(self, e: gmpy2.mpz, n: gmpy2.mpz): # type: ignore
        _, conver_list = ration_to_confrac(e, n)

        for (k, d) in conver_list:
            if k != 0 and (e * d - 1) % k == 0:
                phi = (e * d - 1) // k
                s = n - phi + 1

                # Check if quadratic equation x^2 - s*x + n = 0 has integer roots
                delta = gmpy2.square(s) - 4 * n
                if delta >= 0:

                    # Check if roots are integers
                    t = gmpy2.isqrt(delta)
                    if gmpy2.square(t) == delta and gmpy2.is_even(s + t):
                        return d
        return -1

if __name__ == "__main__":
    wiener = Wiener()

    print(wiener.attack(
        gmpy2.mpz(
            271333247455284399612797200708750772352082780294003637188736819208265316101854484424641054799529080455435709656800782321746925628773824901903245821565748728576832415403521443182011035332724201310759331100627866199727436824056710814158855769293376218520605910943571562233658842860505100444281437980080018597139
            ),
        gmpy2.mpz(
            854334443481063770319788433886224365303189854976858250133365085009109528181563544479498535258353805352625116349824000826129761818874062838363702903729685745574655256076275641217299675240883761187942383878614628978632025302844470289508896272404721947228289320194399047228804666971742127212385133618033283606517
            )))
