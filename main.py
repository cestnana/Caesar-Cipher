#import ascii art
import ascii_art
print(ascii_art.logo)

# Start with 26 English letters List
char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Encrypt function
def encrypt(original_text, shift_amount):
    encrypt_text = []
    for char in original_text:
        if char in char_list:
            char = char.lower()
            current_index = char_list.index(char)
            shifted_index = (current_index + shift_amount) % len(char_list)
            encrypt_text.append(char_list[shifted_index])
        else:
            encrypt_text += char
    result = ''.join(encrypt_text)
    print(f"The Encode Result is: {result}")

# encrypt(original_text=text_input, shift_amount=shift_input)

# Decrypt function
def decrypt(original_text, shift_amount):
    decrypt_text = []
    for char in original_text:
        if char in char_list:
            char = char.lower()
            current_index = char_list.index(char)
            shifted_index = (current_index - shift_amount) % len(char_list)
            decrypt_text.append(char_list[shifted_index])
        else:
            decrypt_text += char
    result = ''.join(decrypt_text)
    print(f"The Decode Result is: {result}")

# decrypt(original_text=text_input, shift_amount=shift_input)

# merged Encrypt/Decrypt function here:
def caesar_cipher(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "decode":
        shift_amount *= -1
        
    output = []
    for char in original_text:
        if char in char_list:
            char = char.lower()
            current_index = char_list.index(char)
            shifted_index = (current_index + shift_amount) % len(char_list)
            output.append(char_list[shifted_index])
        else:
            output += char
    result = ''.join(output)
    print(f"The {encode_or_decode} Result is: {result}")

# save user's input
# func_choice = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
# text_input = input("Type your message:\n").lower()
# shift_input = int(input("Type the shift number:\n"))
    
# Main Logic implementation:
user_continue = "yes"
while user_continue == "yes":

    func_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text_input = input("Type your message:\n").lower()
    shift_input = int(input("Type the shift number:\n"))

    caesar_cipher(original_text=text_input, shift_amount=shift_input, encode_or_decode=func_choice)

    user_continue = input("Type 'yes' if you want to go again. Otherwise, type 'no'")