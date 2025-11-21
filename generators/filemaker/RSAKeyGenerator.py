'''
Created on Dec 14, 2011

@author: pablocelayes
'''
import cryptography, generators
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from generators.low_pr_key_gen import MillerRabin, Arithmetic

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""\

This module generates RSA-keys which are vulnerable to
the Wiener continued fraction attack

(see RSAfracCont.pdf)

The RSA keys are obtained as follows:
1. Choose two prime numbers p and q
2. Compute n=pq
3. Compute phi(n)=(p-1)(q-1)
4. Choose e coprime to phi(n) such that gcd(e,n)=1
5. Compute d = e^(-1) mod (phi(n))
6. e is the publickey; n is also made public (determines the block size); d is the privatekey

Encryption is as follows:
1. Size of data to be encrypted must be less than n
2. ciphertext=pow(plaintext,publickey,n)

Decryption is as follows:
1. Size of data to be decrypted must be less than n
2. plaintext=pow(ciphertext,privatekey,n)

-------------------------------

RSA-keys are Wiener-vulnerable if d < (n^(1/4))/sqrt(6)

"""
from cryptography.hazmat.primitives.asymmetric import rsa
import random

class RSAKeyGenerator:
    def __init__(self, bits = 128):
        self.bits = bits
    def getPrimePair(self):
        '''
        genera un par de primos p , q con
            p de nbits y
            p < q < 2p
        '''

        # assert self.bits // 2 % 4 == 0
        p = MillerRabin.gen_prime(self.bits // 2)
        q = MillerRabin.gen_prime(self.bits // 2)

        return p, q

    def generateKeys(self):
        '''
        Generates a key pair
            public = (e,n)
            private = d
        such that
            n is nbits long
            (e,n) is vulnerable to the Wiener Continued Fraction Attack
        '''
        # nbits >= 1024 is recommended
        # assert self.bits % 4 == 0

        p, q = self.getPrimePair()
        n = p * q
        phi = Arithmetic.totient(p, q)

        # generate a d such that:
        #     (d,n) = 1
        #    36d^4 < n
        good_d = False
        while not good_d:
            d = random.getrandbits(self.bits)
            if (Arithmetic.gcd(d, phi) == 1):  # and 36*pow(d, 4) < n):
                good_d = True

        e = Arithmetic.modInverse(d, phi)
        return e, n


if __name__ == "__main__":
    # print("hey")
    key_gen = RSAKeyGenerator()
    for i in range(1):

        e,n = key_gen.generateKeys()
        public_numbers = rsa.RSAPublicNumbers(e,n)
        public_key = public_numbers.public_key(default_backend())

        pem_private = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # 写入文件
        with open('private_key.pem', 'wb') as f:
            f.write(pem_private)

        with open("private_key.pem", "rb") as f:
            pem_data = f.read()

        # 加载公钥对象
        public_key = serialization.load_pem_public_key(pem_data)

        # 提取公钥参数
        public_numbers = public_key.public_numbers()
        n = public_numbers.n  # 模数
        e = public_numbers.e  # 公钥指数

        print(f"Modulus (n): {n}")
        print(f"Exponent (e): {e}")
        '''
        print ("Clave Publica:")
        print("e =")
        print(e)
        print("n =")
        print(n)
        print ("Clave Privada:")
        print("d =")
        print(d)
        print("-----------------------")
        '''
