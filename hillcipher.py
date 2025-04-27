import numpy as np

def hill_encrypt(text, key):
    text = text.replace(" ", "").lower()
    while len(text) % 2 != 0:
        text += 'x'
    key_matrix = np.array(key).reshape(2, 2)
    encrypted = ""
    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - 97, ord(text[i+1]) - 97]
        result = np.dot(key_matrix, pair) % 26
        encrypted += ''.join([chr(num + 97) for num in result])
    return encrypted

def hill_decrypt(ciphertext, key):
    key_matrix = np.array(key).reshape(2, 2)
    det = int(np.round(np.linalg.det(key_matrix)))  # determinant
    det_inv = pow(det, -1, 26)  # modular inverse of determinant mod 26
    
    # Adjugate matrix for 2x2
    adjugate = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                         [-key_matrix[1][0], key_matrix[0][0]]]) % 26
    
    # Inverse matrix mod 26
    inverse_matrix = (det_inv * adjugate) % 26
    
    decrypted = ""
    for i in range(0, len(ciphertext), 2):
        pair = [ord(ciphertext[i]) - 97, ord(ciphertext[i+1]) - 97]
        result = np.dot(inverse_matrix, pair) % 26
        decrypted += ''.join([chr(int(num) + 97) for num in result])
    return decrypted

# --------- MAIN DRIVER CODE -------------

choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().lower()
text = input("Enter the text: ")
key = list(map(int, input("Enter 4 space-separated integers for key matrix (2x2): ").split()))

if choice == 'e':
    encrypted = hill_encrypt(text, key)
    print("Encrypted Text:", encrypted)
elif choice == 'd':
    decrypted = hill_decrypt(text, key)
    print("Decrypted Text:", decrypted)
else:
    print("Invalid choice! Please enter 'E' or 'D'.")
