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

# Input teks dari pengguna
text = input("Masukkan teks yang akan dienkripsi: ")
shift = int(input("Masukkan jumlah geseran: "))

# Enkripsi teks
encrypted_text = caesar_cipher(text, shift)

print("Teks yang dienkripsi:", encrypted_text)

# Dekripsi teks
decrypted_text = caesar_cipher(encrypted_text, -shift)

print("Teks yang didekripsi:", decrypted_text)
