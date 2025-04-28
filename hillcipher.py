import numpy as np

def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)  
    matrix_mod_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_mod_inv

def encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = plaintext.upper().replace(" ", "")
    while len(plaintext) % n != 0:
        plaintext += 'X'  

    plain_numbers = [ord(c) - ord('A') for c in plaintext]
    cipher_numbers = []

    for i in range(0, len(plain_numbers), n):
        block = np.array(plain_numbers[i:i+n]).reshape(n, 1)
        cipher_block = np.dot(key_matrix, block) % 26
        cipher_numbers.extend(cipher_block.flatten())

    ciphertext = ''.join(chr(num + ord('A')) for num in cipher_numbers)
    return ciphertext

def decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    cipher_numbers = [ord(c) - ord('A') for c in ciphertext]
    key_matrix_inv = matrix_mod_inverse(key_matrix, 26)
    plain_numbers = []

    for i in range(0, len(cipher_numbers), n):
        block = np.array(cipher_numbers[i:i+n]).reshape(n, 1)
        plain_block = np.dot(key_matrix_inv, block) % 26
        plain_numbers.extend(plain_block.flatten())

    plaintext = ''.join(chr(int(num) + ord('A')) for num in plain_numbers)
    return plaintext

plaintext = input("Enter the plaintext: ")

n = int(input("Enter the size of the key matrix (n for n x n matrix): "))
print(f"Enter the {n}x{n} key matrix row by row (space-separated numbers):")
key_elements = []
for _ in range(n):
    row = list(map(int, input().split()))
    key_elements.append(row)

key_matrix = np.array(key_elements)

ciphertext = encrypt(plaintext, key_matrix)
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, key_matrix)
print(f"Decrypted text: {decrypted_text}")
