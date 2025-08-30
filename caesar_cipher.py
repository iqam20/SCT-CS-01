# caesar_cipher.py

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


if __name__ == "__main__":
    print("=== Caesar Cipher Program ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice.startswith("e"):
        encrypted = encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice.startswith("d"):
        decrypted = decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid choice! Please select Encrypt or Decrypt.")
