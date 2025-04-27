def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) - shift + 26) % 26 + ord(base))
            key_index += 1
        else:
            result += char
    return result

# --------- MAIN DRIVER CODE -------------

choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().lower()
text = input("Enter the text: ")
key = input("Enter the key: ")

if choice == 'e':
    encrypted = vigenere_encrypt(text, key)
    print("Encrypted Text:", encrypted)
elif choice == 'd':
    decrypted = vigenere_decrypt(text, key)
    print("Decrypted Text:", decrypted)
else:
    print("Invalid choice! Please enter 'E' or 'D'.")
