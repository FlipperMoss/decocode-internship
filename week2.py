message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = ""
decrypted = ""

for char in message:
    if char.isupper():
        cipher_char = chr((ord(char) - 65 + shift) % 26 + 65)
        encrypted += cipher_char
    
    elif char.islower():
        cipher_char = chr((ord(char) - 97 + shift) % 26 + 97)
        encrypted += cipher_char
    
    else:
        encrypted += char
        
for char in encrypted:
    if char.isupper():
        plain_char = chr((ord(char) - 65 - shift) % 26 + 65)
        decrypted += plain_char
    
    elif char.islower():
        plain_char = chr((ord(char) - 97 - shift) % 26 + 97)
        decrypted += plain_char
        
    else:
        decrypted += char

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)