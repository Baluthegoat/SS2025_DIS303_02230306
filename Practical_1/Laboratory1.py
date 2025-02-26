def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text : 
        if char.isalpha() :
            shifted = ord(char) + shift 
            if char.islower() :
                if shifted > ord('Z'):
                    shifted -= 26
            elif char.isupper() :
                if shifted > ord('Z') :
                    shifted -= 26
            encrypted_text += chr(shifted)
        else : 
            encrypted_text += char
    return encrypted_text

def ceaser_decrypt(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if shifted < ord('a'):
                shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text 

message = "Foundation"
shift = 5

encrypted_message = caesar_encrypt(message, shift)
print("Encrypted Message:", encrypted_message)

decrypted_message = caesar_encrypt(encrypted_message, shift)
print("Decrypted Message:", decrypted_message)