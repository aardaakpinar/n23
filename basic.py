import random
import math

def encrypt(text):
    encrypted_hex = []

    salt = random.randint(1000, 9999)
    encrypted_hex.append(hex(salt)[2:].upper())

    key = (ord(text[0]) + 23 + salt) ** 3
    encrypted_hex.append(hex(key)[2:].upper())

    for i in range(1, len(text)):
        key = key + i + ord(text[i])
        encrypted_hex.append(hex(key)[2:].upper())

    return ":".join(encrypted_hex)


def decrypt(hex_string):
    parts = hex_string.split(":")

    salt = int(parts[0], 16)
    values = [int(p, 16) for p in parts[1:]]

    first_key = values[0]
    first_char_code = round(first_key ** (1/3)) - 23 - salt
    text = chr(first_char_code)

    prev = first_key
    for i in range(1, len(values)):
        cur = values[i]
        char_code = cur - prev - i
        text += chr(char_code)
        prev = cur

    return text


def main():
    print("=== N23 ===")
    print("1) Encrypt")
    print("2) Decrypt")
    choice = input("Select: ").strip()

    if choice == "1":
        text = input("Text: ")
        result = encrypt(text)
        print("\nOut:", result)

    elif choice == "2":
        hex_string = input("Hex: ")
        try:
            result = decrypt(hex_string)
            print("\nOut:", result)
        except Exception:
            print("\nError")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
