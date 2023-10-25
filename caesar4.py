def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) + shift - ord('a')
            shifted %= 26
            shifted += ord('a')
            
            if is_upper:
                char = chr(shifted).upper()
            else:
                char = chr(shifted)
        
        result += char

    return result

def vigenere_cipher(text, key):
    result = ""
    key = key.lower()  # Konversi kunci menjadi huruf kecil
    
    for i, char in enumerate(text):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            key_shift = ord(key[i % len(key)]) - ord('a')
            shifted = ord(char) + key_shift - ord('a')
            shifted %= 26
            shifted += ord('a')
            
            if is_upper:
                char = chr(shifted).upper()
            else:
                char = chr(shifted)
        
        result += char

    return result

# Input teks dari pengguna
text = input("Masukkan teks yang akan dienkripsi: ")
shift = int(input("Masukkan jumlah geseran Caesar Cipher: "))
key = input("Masukkan kunci Vigenere Cipher: ")

# Enkripsi teks menggunakan Caesar Cipher
caesar_encrypted_text = caesar_cipher(text, shift)

# Enkripsi teks menggunakan Vigenere Cipher setelah Caesar Cipher
encrypted_text = vigenere_cipher(caesar_encrypted_text, key)

print("Teks yang dienkripsi:", encrypted_text)
