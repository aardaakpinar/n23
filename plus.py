import random
import hashlib

def _sha256_bytes(s: str) -> bytes:
    return hashlib.sha256(s.encode("utf-8")).digest()

def _int_cuberoot(n: int) -> int:
    if n < 0:
        raise ValueError("negative not supported")
    if n < 8:
        return 0 if n == 0 else 1
    r = int(n ** (1/3))
    while (r + 1) ** 3 <= n:
        r += 1
    while r ** 3 > n:
        r -= 1
    return r

def encrypt(text: str, key: str) -> str:
    if not text:
        return ""
    key_bytes = _sha256_bytes(key)
    salt = random.randint(1000, 9999)
    parts = [format(salt, "X").upper()]

    tweak0 = int.from_bytes(key_bytes[:2], "big")

    first_val = (ord(text[0]) + 23 + salt + tweak0) ** 3
    parts.append(format(first_val, "X").upper())

    prev = first_val
    for i in range(1, len(text)):
        char_code = ord(text[i])
        tweak = key_bytes[i % len(key_bytes)]
        cur = prev + i + char_code + tweak
        parts.append(format(cur, "X").upper())
        prev = cur

    return ":".join(parts)

def decrypt(hex_string: str, key: str) -> str:
    if not hex_string:
        return ""
    raw_parts = hex_string.split(":")
    salt = int(raw_parts[0], 16)
    values = [int(p, 16) for p in raw_parts[1:]]

    key_bytes = _sha256_bytes(key)
    tweak0 = int.from_bytes(key_bytes[:2], "big")

    first_key = values[0]
    root = _int_cuberoot(first_key)
    first_char_code = root - 23 - salt - tweak0
    text_chars = [chr(first_char_code)]

    prev = first_key
    for i in range(1, len(values)):
        cur = values[i]
        tweak = key_bytes[i % len(key_bytes)]
        char_code = cur - prev - i - tweak
        text_chars.append(chr(char_code))
        prev = cur

    return "".join(text_chars)

def main():
    print("=== N23+ ===")
    print("1) Encrypt")
    print("2) Decrypt")
    choice = input("Select: ").strip()

    if choice == "1":
        text = input("Text: ")
        key = input("Key: ")
        print("\nOut:", encrypt(text, key))

    elif choice == "2":
        hex_string = input("Hex: ")
        key = input("Key: ")
        try:
            print("\nOut:", decrypt(hex_string, key))
        except Exception:
            print("\nError")

    else:
        print("Invalid")

if __name__ == "__main__":
    main()
