def generate_playfair_matrix(key):
    matrix = []
    key = key.lower().replace('j', 'i')
    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)
    for char in 'abcdefghiklmnopqrstuvwxyz':  # Notice 'j' is excluded
        if char not in matrix:
            matrix.append(char)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(text, key):
    text = text.lower().replace('j', 'i')
    text = ''.join(filter(str.isalpha, text))
    if len(text) % 2 != 0:
        text += 'x'
    digraphs = [text[i:i+2] for i in range(0, len(text), 2)]

    matrix = generate_playfair_matrix(key)
    cipher = ''
    for a, b in digraphs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            cipher += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            cipher += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            cipher += matrix[row1][col2] + matrix[row2][col1]
    return cipher

def playfair_decrypt(cipher, key):
    cipher = cipher.lower().replace('j', 'i')
    cipher = ''.join(filter(str.isalpha, cipher))
    digraphs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]

    matrix = generate_playfair_matrix(key)
    decrypted = ''
    for a, b in digraphs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            decrypted += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            decrypted += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            decrypted += matrix[row1][col2] + matrix[row2][col1]
    return decrypted

# --------- MAIN DRIVER CODE --------------

choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().lower()
text = input("Enter the text (alphabets only): ")
key = input("Enter the key: ")

if choice == 'e':
    encrypted = playfair_encrypt(text, key)
    print("Encrypted Text:", encrypted)
elif choice == 'd':
    decrypted = playfair_decrypt(text, key)
    print("Decrypted Text:", decrypted)
else:
    print("Invalid choice! Please enter 'E' or 'D'.")
