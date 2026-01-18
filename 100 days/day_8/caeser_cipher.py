alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(original_text, shift_amount, encode_decode):
    cipher_text = ""
    if encode_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_decode} message: {cipher_text}")
continue_program = True
while continue_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(original_text=text, shift_amount=shift, encode_decode=direction)
    restart=input("Type 'yes' if you want to go again.Otherwise type 'no'.\n").lower()
    if restart == "no":
        continue_program = False
        print("Goodbye!")
