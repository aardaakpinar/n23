import random
import math

def encrypt(text):
    encrypted_hex = []

    # Salt (16-bit)
    salt = random.randint(1000, 9999)
    encrypted_hex.append(hex(salt)[2:].upper())

    # First character: (ord + 23 + salt)^3
    key = (ord(text[0]) + 23 + salt) ** 3
    encrypted_hex.append(hex(key)[2:].upper())

    # Chained value generation
    for i in range(1, len(text)):
        key = key + i + ord(text[i])
        encrypted_hex.append(hex(key)[2:].upper())

    return ":".join(encrypted_hex)


def decrypt(hex_string):
    parts = hex_string.split(":")

    # Extract salt
    salt = int(parts[0], 16)

    # Convert remaining HEX parts to integers
    values = [int(p, 16) for p in parts[1:]]

    # First character
    first_key = values[0]
    first_char_code = round(first_key ** (1/3)) - 23 - salt
    text = chr(first_char_code)

    # Reverse chain
    prev = first_key
    for i in range(1, len(values)):
        cur = values[i]
        char_code = cur - prev - i
        text += chr(char_code)
        prev = cur

    return text


def main():
    print("=== N23+ Crypto ===")
    print("1) Encrypt")
    print("2) Decrypt")
    choice = input("Select (1/2): ")

    if choice == "1":
        text = input("Enter text to encrypt: ")
        result = encrypt(text)
        print("\nEncrypted:", result)

    elif choice == "2":
        text = input("Enter HEX string to decrypt: ")
        result = decrypt(text)
        print("\nDecrypted:", result)

    else:
        print("Invalid selection!")


if __name__ == "__main__":
    main()