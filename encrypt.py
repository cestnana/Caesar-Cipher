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

encrypt(original_text=text_input, shift_amount=shift_input)