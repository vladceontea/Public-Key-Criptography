"""
This function computes the product between the message matrix and the key matrix, which is the matrix of the cipher.
"""
def encrypt(message_matrix, key_matrix, cipher_matrix):
    for i in range(2):
        for j in range(2):
            for x in range(2):
                cipher_matrix[i][j] += (message_matrix[i][x] * key_matrix[x][j])
            cipher_matrix[i][j] = cipher_matrix[i][j] % 27
            # The modulo 27 is used to only have values from 1 - 26, representing the alphabet (1 - A, 26 - Z)

    return cipher_matrix


"""
This function computes the product between the cipher matrix and the inverse key matrix, which is the matrix of the original message.
"""
def decrypt(decrypted_message_matrix, inv_key_matrix, cipher_matrix):
    for i in range(2):
        for j in range(2):
            for x in range(2):
                decrypted_message_matrix[i][j] += (cipher_matrix[i][x] * inv_key_matrix[x][j])
            decrypted_message_matrix[i][j] = decrypted_message_matrix[i][j] % 27
            # The modulo 27 is used to only have values from 1 - 26, representing the alphabet (1 - A, 26 - Z)

    return decrypted_message_matrix


"""
This function computes the inverse of a matrix
"""
def inverse_matrix(key):

    key_determinant = (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 27

    inv_determinant = pow(key_determinant, -1, 27)

    inv_key_matrix = [[key_matrix[1][1] % 27, (-key_matrix[0][1]) % 27], [(-key_matrix[1][0]) % 27, key_matrix[0][0] % 27]]

    for i in range(2):
        for j in range(2):
            inv_key_matrix[i][j] = inv_key_matrix[i][j] * inv_determinant % 27

    return inv_key_matrix


"""
This function transform the message in a matrix, computes the cipher matrix with the help of the encrypt function and prints the cipher message.
"""
def HillCipher(message, key):
    cipher_matrix = [[0, 0] for _ in range(2)]
    message_matrix = [[0, 0] for _ in range(2)]
    decrypted_message_matrix = [[0, 0] for _ in range(2)]
    inv_key_matrix = [[0, 0] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            message_matrix[i][j] = ord(message[i*2+j]) - 64

    cipher_matrix = encrypt(message_matrix, key, cipher_matrix)

    cipher = []
    for i in range(2):
        for j in range(2):
            cipher.append(chr(cipher_matrix[i][j] + 64))

    print("Ciphertext:", "".join(cipher))

    inv_key_matrix = inverse_matrix(key)

    decrypted_message_matrix = decrypt(decrypted_message_matrix, inv_key_matrix, cipher_matrix)

    decrypted_message = []
    for i in range(2):
        for j in range(2):
            decrypted_message.append(chr(decrypted_message_matrix[i][j] + 64))

    print("Decrypted message:", "".join(decrypted_message))


if __name__ == "__main__":

    message = "FOUR"
    print("Message: " + message)
    key_matrix = [[11, 8], [3, 7]]

    HillCipher(message, key_matrix)
