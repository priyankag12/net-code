def columnar_transposition_encrypt(text, key):
    text = text.replace(" ", "")
    col = len(key)
    row = len(text) // col + (len(text) % col > 0)
    grid = [['' for _ in range(col)] for _ in range(row)]
    
    idx = 0
    for i in range(row):
        for j in range(col):
            if idx < len(text):
                grid[i][j] = text[idx]
                idx += 1

    order = sorted(list(enumerate(key)), key=lambda x: x[1])
    encrypted = ''
    for i, _ in order:
        for j in range(row):
            if grid[j][i] != '':
                encrypted += grid[j][i]
    return encrypted

def columnar_transposition_decrypt(ciphertext, key):
    col = len(key)
    row = len(ciphertext) // col + (len(ciphertext) % col > 0)
    num_full_cols = len(ciphertext) % col
    grid = [['' for _ in range(col)] for _ in range(row)]

    order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    idx = 0
    for i, _ in order:
        current_col_len = row if i < num_full_cols or num_full_cols == 0 else row - 1
        for j in range(current_col_len):
            if idx < len(ciphertext):
                grid[j][i] = ciphertext[idx]
                idx += 1

    decrypted = ''
    for i in range(row):
        for j in range(col):
            if grid[i][j] != '':
                decrypted += grid[i][j]
    return decrypted

# --------- MAIN DRIVER CODE -------------

choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().lower()
text = input("Enter the text: ")
key = input("Enter the key (as string): ")

if choice == 'e':
    encrypted = columnar_transposition_encrypt(text, key)
    print("Encrypted Text:", encrypted)
elif choice == 'd':
    decrypted = columnar_transposition_decrypt(text, key)
    print("Decrypted Text:", decrypted)
else:
    print("Invalid choice! Please enter 'E' or 'D'.")
