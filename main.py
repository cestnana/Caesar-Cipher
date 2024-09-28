# Start with 26 English letters
char_collection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# func_choice = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
original_text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount, char_collection):
    encrypt_text = []
    for char in original_text:
        if char in char_collection:
            char = char.lower()
            index = char_collection.index(char)
            shifted_index = (index + shift_amount) % len(char_collection)
            encrypt_text.append(char_collection[shifted_index])
            # print(encrypt_text)
        else:
            encrypt_text = char
    # print("".join(encrypt_text))
    return ''.join(encrypt_text)


encrypt(original_text, shift_amount, char_collection)