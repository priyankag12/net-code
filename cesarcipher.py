def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

choice = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().lower()
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

if choice == 'e':
    encrypted = caesar_cipher(text, shift, mode='encrypt')
    print("Encrypted Text:", encrypted)
elif choice == 'd':
    decrypted = caesar_cipher(text, shift, mode='decrypt')
    print("Decrypted Text:", decrypted)
else:
    print("Invalid choice! Please enter 'E' or 'D'.")
