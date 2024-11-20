def encrypt_message(message):
     # Define the encryption mapping
    encryption_map = {
        "D": "S",
        "a": "5",
        "t": "@",
        "e": "#"
    }
    
    # Encrypt the message
    encrypted_message = ""
    for char in message:
        if encryption_map[char]:
            encrypted_message += encryption_map[char]
        else:
            encrypted_message += char
        # encrypted_message += encryption_map[char] if char in encryption_map else char
    return encrypted_message

message = input("Enter the message to encrypt: ")
print("Encrypted message:", encrypt_message(message))
