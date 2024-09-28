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

decrypt(original_text=text_input, shift_amount=shift_input)