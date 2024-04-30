def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isupper():
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message
message = input("Enter message to encrypt: ")
shift = int(input("Enter shift value: "))
encrypted_message = caesar_cipher_encrypt(message, shift)
print("Encrypted message:", encrypted_message)
