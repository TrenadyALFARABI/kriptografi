def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.upper()) - ord('A')
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - key_shift - ord('A')) % 26 + ord('A'))
            else:
                plaintext += chr((ord(ciphertext[i]) - key_shift - ord('a')) % 26 + ord('a'))
        else:
            plaintext += ciphertext[i]

    return plaintext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
        else:
            plaintext += char

    return plaintext

if __name__ == "__main__":
    ciphertext = input("Masukkan teks sandi: ")
    vigenere_key = input("Masukkan kunci Vigenere: ")
    caesar_shift = int(input("Masukkan pergeseran Caesar: "))

    vigenere_decrypted_text = vigenere_decrypt(ciphertext, vigenere_key)
    caesar_decrypted_text = caesar_decrypt(vigenere_decrypted_text, caesar_shift)

    print("Hasil dekripsi Caesar Cipher: " + caesar_decrypted_text)
