# generate key

import random
import sympy


alphabet = {" ": 0, "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
inv_alphabet = {v: k for k, v in alphabet.items()}

def gen_key(q):
    # generate random prime p
    p = sympy.prevprime(q)  # generate a large prime number

    g = random.randrange(2, p - 1)  # generate a generator of Zp

    a = random.randrange(1, p - 2)  # select a random integer between 1 and p-2

    y = pow(g, a, p)

    return a, y, p, g  # return the private key a and the public key


# encryption
def encrypt_elgamal(p, g, y, msg):
    binary = ''.join('{0:08b}'.format(alphabet[x], 'b') for x in msg)
    m = int(binary, 2)  # represent the message as a number

    k = random.randrange(1, p - 2)  # select a random integer between 1 and p-2

    alpha = pow(g, k, p)
    beta = (m * pow(y, k, p)) % p
    #  create the ciphertext (alpha, beta)

    return alpha, beta


# decryption
def decrypt_elgamal(alpha, beta, a, p):
    m = (beta * pow(alpha, p - 1 - a, p)) % p
    binary = bin(m)
    binary = binary.replace('b', '')
    while len(binary) % 8 != 0:
        binary = "0" + binary

    message = ''.join(inv_alphabet[int(binary[i:i+8], 2)] for i in range(0, len(binary), 8))
    #  decrypt the ciphertext with the help of the private key

    return message


if __name__ == "__main__":
    msg = input("Enter message: ")
    while not all(c in alphabet for c in msg):
        print("Not a valid message")
        msg = input("Enter message: ")

    q = random.randint(pow(10, 20), pow(10, 50))
    a, y, p, g = gen_key(q)
    alpha, beta = encrypt_elgamal(p, g, y, msg)

    message = decrypt_elgamal(alpha, beta, a, p)

    print("Decrypted message: " + message)
