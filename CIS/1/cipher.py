def cipher(text,shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
        
    return result
    
message = input("Enter the text to encrypt: ")
Shift = 3

encrypted_message = cipher(message, Shift)
print("Encrypted: ", encrypted_message)

decrypted_message = cipher(encrypted_message, -Shift)
print("Decrypted: ", decrypted_message)
