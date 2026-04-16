
def encrypt_char(ch: str, shift1: int, shift2: int) -> tuple:
    """
    Encrypt a single character according to the assignment rules.

    Returns:
        (encrypted_char, bucket_flag)
        bucket_flag is '0' or '1' for alpha chars, '' for non-alpha.
    """
    if ch.islower():
        offset = ord(ch) - ord('a')          # 0-25
        if offset <= 12:                      # a-m -> shift forward
            new_offset = (offset + shift1 * shift2) % 26
            return chr(new_offset + ord('a')), '0'
        else:                                 # n-z -> shift backward
            new_offset = (offset - (shift1 + shift2)) % 26
            return chr(new_offset + ord('a')), '1'

    elif ch.isupper():
        offset = ord(ch) - ord('A')          # 0-25
        if offset <= 12:                      # A-M -> shift backward
            new_offset = (offset - shift1) % 26
            return chr(new_offset + ord('A')), '0'
        else:                                 # N-Z -> shift forward
            new_offset = (offset + shift2 ** 2) % 26
            return chr(new_offset + ord('A')), '1'

    else:
        return ch, ''                         # non-alpha: unchanged, no flag


def decrypt_char(ch: str, bucket: str, shift1: int, shift2: int) -> str:
    """
    Decrypt a single character using the stored bucket flag.

    bucket: '0' means first-half rule was applied, '1' means second-half rule.
    """
    if ch.islower():
        offset = ord(ch) - ord('a')
        if bucket == '0':                     # was a-m: reverse forward shift
            new_offset = (offset - shift1 * shift2) % 26
        else:                                 # was n-z: reverse backward shift
            new_offset = (offset + (shift1 + shift2)) % 26
        return chr(new_offset + ord('a'))

    elif ch.isupper():
        offset = ord(ch) - ord('A')
        if bucket == '0':                     # was A-M: reverse backward shift
            new_offset = (offset + shift1) % 26
        else:                                 # was N-Z: reverse forward shift
            new_offset = (offset - shift2 ** 2) % 26
        return chr(new_offset + ord('A'))

    else:
        return ch                             # non-alpha: unchanged



def encrypt(shift1: int, shift2: int,
            input_file:  str = "raw_text.txt",
            output_file: str = "encrypted_text.txt") -> None:
    """
    Read plain text from input_file, apply the assignment encryption rules,
    and write the result to output_file.

    The output file format is:  <bucket_flags>|<cipher_text>
    where bucket_flags is a compact string of '0'/'1' characters (one per
    alphabetic character in the original text).
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            plain_text = f.read()
    except FileNotFoundError:
        print(f"[ERROR] '{input_file}' not found. "
              "Make sure it is in the same folder as this script.")
        return

    bucket_flags = []
    cipher_chars = []

    for ch in plain_text:
        enc_ch, flag = encrypt_char(ch, shift1, shift2)
        cipher_chars.append(enc_ch)
        if flag:                              # only alpha chars get a flag
            bucket_flags.append(flag)

    # Build the output: bucket metadata prefix + pipe separator + cipher text
    output = ''.join(bucket_flags) + '|' + ''.join(cipher_chars)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"[OK] Encryption complete  -->  '{output_file}' written.")


def decrypt(shift1: int, shift2: int,
            input_file:  str = "encrypted_text.txt",
            output_file: str = "decrypted_text.txt") -> None:
    """
    Read the encrypted file (format: <bucket_flags>|<cipher_text>),
    apply the inverse shifts guided by the stored bucket flags, and write
    the recovered plain text to output_file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            raw = f.read()
    except FileNotFoundError:
        print(f"[ERROR] '{input_file}' not found. Run encryption first.")
        return

    # Split on the FIRST pipe character
    if '|' not in raw:
        print("[ERROR] Encrypted file is missing the bucket-flag prefix. "
              "Was it created by this program?")
        return

    pipe_pos    = raw.index('|')
    bucket_flags = raw[:pipe_pos]            # e.g. '010011...'
    cipher_text  = raw[pipe_pos + 1:]        # the actual cipher characters

    # Reconstruct plain text
    decrypted_chars = []
    flag_index = 0                           # pointer into bucket_flags

    for ch in cipher_text:
        if ch.isalpha():
            bucket = bucket_flags[flag_index]
            flag_index += 1
            decrypted_chars.append(decrypt_char(ch, bucket, shift1, shift2))
        else:
            decrypted_chars.append(ch)       # non-alpha passes through

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(decrypted_chars))

    print(f"[OK] Decryption complete  -->  '{output_file}' written.")


def verify(original_file:  str = "raw_text.txt",
           decrypted_file: str = "decrypted_text.txt") -> bool:
    """
    Compare original_file with decrypted_file character by character.

    Prints a PASS or FAIL message with a brief diff summary on failure.
    Returns True if the files are identical, False otherwise.
    """
    try:
        with open(original_file, 'r', encoding='utf-8') as f:
            original = f.read()
        with open(decrypted_file, 'r', encoding='utf-8') as f:
            decrypted = f.read()
    except FileNotFoundError as e:
        print(f"[ERROR] Verification failed - file not found: {e}")
        return False

    if original == decrypted:
        print("[OK] VERIFICATION PASSED: "
              "Decrypted text matches the original perfectly!")
        return True

    #  Detailed failure report
    print("[FAIL] VERIFICATION FAILED: "
          "Decrypted text does NOT match the original.")

    min_len = min(len(original), len(decrypted))
    mismatches = [
        (i, original[i], decrypted[i])
        for i in range(min_len)
        if original[i] != decrypted[i]
    ]

    print(f"  Character mismatches : {len(mismatches)}")
    print(f"  Length - original    : {len(original)}")
    print(f"  Length - decrypted   : {len(decrypted)}")

    if mismatches:
        print("  First 5 mismatches  (position | expected | got):")
        for pos, exp, got in mismatches[:5]:
            print(f"    pos {pos:>4}:  "
                  f"expected {repr(exp):>6}  got {repr(got):>6}")

    return False


def get_positive_integer(prompt: str) -> int:
    """Keep prompting until the user enters a valid positive integer."""
    while True:
        raw = input(prompt).strip()
        if raw.lstrip('-').isdigit():
            value = int(raw)
            if value > 0:
                return value
            print("    Please enter a positive integer (greater than 0).")
        else:
            print("    Invalid input. Please enter a whole number (e.g. 3).")


def main():
    print("=" * 55)
    print("  HIT137 Assignment 2  |  Q1: Encrypt / Decrypt")
    print("=" * 55)

    # Step 1 – Collect shift values from the user
    print("\nProvide two positive integer shift values.\n")
    shift1 = get_positive_integer("  Enter shift1: ")
    shift2 = get_positive_integer("  Enter shift2: ")
    print(f"\n  Using  shift1 = {shift1},  shift2 = {shift2}")
    print("-" * 55)

    # Step 2 – Encrypt raw_text.txt    encrypted_text.txt
    print("\n[Step 1]  Encrypting 'raw_text.txt' ...")
    encrypt(shift1, shift2)

    # Step 3 – Decrypt encrypted_text.txt    decrypted_text.txt
    print("\n[Step 2]  Decrypting 'encrypted_text.txt' ...")
    decrypt(shift1, shift2)

    # Step 4 – Verify raw_text.txt == decrypted_text.txt
    print("\n[Step 3]  Verifying decryption ...")
    verify()

    print("\n" + "=" * 55)
    print("  Files produced:")
    print("    encrypted_text.txt  –  cipher text (with bucket metadata)")
    print("    decrypted_text.txt  –  recovered plain text")
    print("=" * 55)


if __name__ == "__main__":
    main()
