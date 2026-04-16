import string

def shift_char(c, shift):
    if c.isalpha():
        base = ord('a') if c.islower() else ord('A')
        return chr((ord(c) - base + shift) % 26 + base)
    return c


def encrypt(text, shift1, shift2):
    result = ""

    for c in text:
        if c.islower():
            if c <= 'm':
                result += shift_char(c, shift1 * shift2)
            else:
                result += shift_char(c, -(shift1 + shift2))

        elif c.isupper():
            if c <= 'M':
                result += shift_char(c, -shift1)
            else:
                result += shift_char(c, shift2 ** 2)
        else:
            result += c

    return result


def decrypt(text, shift1, shift2):
    result = ""

    for c in text:
        if c.islower():
            if c <= 'm':
                result += shift_char(c, -(shift1 * shift2))
            else:
                result += shift_char(c, (shift1 + shift2))

        elif c.isupper():
            if c <= 'M':
                result += shift_char(c, shift1)
            else:
                result += shift_char(c, -(shift2 ** 2))
        else:
            result += c

    return result


def verify(original, decrypted):
    return original == decrypted


def main():
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    with open("raw_text.txt", "r") as f:
        text = f.read()

    encrypted = encrypt(text, shift1, shift2)

    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)

    decrypted = decrypt(encrypted, shift1, shift2)

    with open("decrypted_text.txt", "w") as f:
        f.write(decrypted)

    if verify(text, decrypted):
        print("✅ Decryption successful!")
    else:
        print("❌ Decryption failed!")


if __name__ == "__main__":
    main()