import math
import random
import sys

from numpy import long


def is_prime(num):
    for i in range(int(math.floor(float(num) / 2)) + 1)[2:]:

        if num % i == 0:
            return False

    return True


def random_prime(low=0, high=100):
    '''

    to get prime randomly

    low: lower bound of range

    high: higher bound of range

    '''

    rand = random.randint(low, high)

    while (True):  # is prime or not

        if not is_prime(rand):

            rand = (rand + 1) % (high - low) + low

        else:

            return rand


def gcd(a, b):
    '''

    get gcd from a and b

    '''

    if a < b:
        a, b = b, a

    while b:
        a, b = b, a % b

    return a


def egcd(a, b):
    '''

    Extended Euclidean Algorithm

    returns x, y, gcd(a,b) such that ax + by = gcd(a,b)

    '''

    u, u1 = 1, 0

    v, v1 = 0, 1

    while b:
        q = a // b

        u, u1 = u1, u - q * u1

        v, v1 = v1, v - q * v1

        a, b = b, a - q * b

    return u, v, a


def modInverse(e, n):
    '''

    d such that de = 1 (mod n)

    e must be coprime to n

    this is assumed to be true

    '''

    return egcd(e, n)[0] % n


def generate_key(e):
    p = random_prime(1000, 2000)  # get p and q, to make p and q big enough

    q = random_prime(1000, 2000)  # such that e < euler_n

    n = p * q  # n equal to p * q

    euler_n = (p - 1) * (q - 1)  # euler(n) = (p - 1)(q - 1)

    # adjusting e

    while gcd(euler_n, e) != 1:
        e += 2  # keep it odd

    d = modInverse(e, euler_n)

    return e, d, n


def rsa_encrypt(e, n, msg):
    '''

    e: such that ed mod(n) = 1, public, chosen

    n: equal to p * q

    msg: needs encrypting

    return: list with dicimal digits, from elements in msg after encrypted

    '''

    cmsg = []

    for elem in msg:
        cmsg.append(pow(ord(elem), e, n))

    return cmsg


def rsa_dencrypt(d, n, cmsg):
    '''

    d: such that ed mod(n) = 1, private, calculated

    n: equal to p * q

    cmsg: list with dicimal digits, from elements in msg after encrypted

    '''

    msg = []

    for elem in cmsg:
        msg.append("%c" % pow(elem, d, n))

    return "".join(msg)


if __name__ == "__main__":

    while (True):

        print("##############menu###############")

        print("1.generate keys")

        print("2.encryption")

        print("3.decryption")

        print("other for quit")

        chose = input("input your choice:")

        if chose == 1:

            e, d, n = generate_key(65537)

            print("generate keys as follow:")

            print("e = %d, d = %d, n = %d" % (e, d, n))

            print("public key(e, n) = (%d, %d), private key(%d, %d)" % (e, n, d, n))

        elif chose == 2:

            msg = input("input your message:")

            e, n = input("input the public key(with format \"e,n\"):")

            sys.stdout.write("ciphertext:")

            for elem in rsa_encrypt(e, n, msg):
                sys.stdout.write(" %d" % elem)

            sys.stdout.write("\n")

        elif chose == 3:

            cmsg_str = input("input your ciphertext:")

            d, n = input("input the private key(with format \"d,n\"):")

            cmsg = []

            for elem in cmsg_str.split(" "):
                cmsg.append(long(elem))

            print("plaintext:", rsa_dencrypt(d, n, cmsg))

        else:
            break


