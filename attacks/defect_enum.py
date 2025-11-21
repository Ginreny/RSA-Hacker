import enum, attacks
from enum import Enum, auto

from attacks.single_key.factordb_attack import Factordb
from attacks.single_key.low_public_key_attack import LowPublicKey
from attacks.single_key.pollard_p_1_attack import PollardP_1
from attacks.single_key.wiener_attack import Wiener
from attacks.single_key.williams_pp1_attack import WilliamsPP1


class DefectEnum(Enum):
    LOW_PRIVATE_KEY = auto()
    P_1_SMOOTH = auto()
    PP_1_SMOOTH = auto()
    SMALL_N = auto()

    def get_name(self):
        return_value = None
        match self:
            case self.LOW_PRIVATE_KEY:
                return_value = "Low_Private_Key"
            case self.P_1_SMOOTH:
                return_value = "Small_Factors_For_p-1"
            case self.PP_1_SMOOTH:
                return_value = "Small_Factors_For_p+1"
            case self.SMALL_N:
                return_value = "Low_Module(<2^16)"

        return return_value

    def get_instance(self):
        return_value = None
        match self:
            case self.LOW_PRIVATE_KEY:
                return_value = Wiener()
            case self.P_1_SMOOTH:
                return_value = PollardP_1()
            case self.PP_1_SMOOTH:
                return_value = WilliamsPP1()
            case self.LOW_PUBLIC_KEY:
                return_value = LowPublicKey()
            case self.SMALL_N:
                return_value = Factordb()

        return return_value
