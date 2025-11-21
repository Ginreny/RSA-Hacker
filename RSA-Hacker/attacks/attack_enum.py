import enum, attacks
from enum import Enum, auto

from attacks.single_key.solution import Solution
from attacks.single_key.dixon_attack import Dixon
from attacks.single_key.ecm_attack import ECMAttack
from attacks.single_key.factordb_attack import Factordb
from attacks.single_key.Fermat2 import Fermat2
from attacks.single_key.fermat1 import Fermat1
from attacks.single_key.pollard_p_1_attack import PollardP_1
from attacks.single_key.pollard_rho_attack import PollardRho
from attacks.single_key.siqs_attack import SIQsieve
from attacks.single_key.wiener_attack import Wiener
from attacks.single_key.williams_pp1_attack import WilliamsPP1


class AttackEnum(Enum):
    DIXON = auto()
    ECM = auto()
    FACTORDB = auto()
    FERMAT1 = auto()
    FERMAT2 = auto()
    POLLARD_P_1 = auto()
    POLLARD_RHO = auto()
    SIQS = auto()
    WIENER = auto()
    WILLIAMS_PP1 = auto()
    SOLUTION = auto()

    def get_instance(self):
        return_value = None
        match self:
            case self.DIXON:
                return_value = Dixon()
            case self.ECM:
                return_value = ECMAttack()
            case self.FACTORDB:
                return_value = Factordb()
            case self.FERMAT1:
                return_value = Fermat1()
            case self.FERMAT2:
                return_value = Fermat2()
            case self.POLLARD_P_1:
                return_value = PollardP_1()
            case self.POLLARD_RHO:
                return_value = PollardRho()
            case self.SIQS:
                return_value = SIQsieve()
            case self.WIENER:
                return_value = Wiener()
            case self.WILLIAMS_PP1:
                return_value = WilliamsPP1()
            case self.SOLUTION:
                return_value = Solution()

        return return_value
