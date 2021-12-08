from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cypher_direction, start_text, shift_amount):
    end_text = ""
    if cypher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            index = index + shift_amount
            index = index % len(alphabet)
            end_text += alphabet[index]
        else:
            end_text += letter
    print(f"The {cypher_direction}d text is {end_text}")

print(logo)
conti = "y"
while conti == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(cypher_direction=direction, start_text=text, shift_amount=shift)
    conti = (input("Do you want to run the caesar cypher again? Y/N")).lower()

""" def encrypt(plain_text, shift_amount):

    encrypted_text = ""
    for letter in plain_text:
        index = alphabet.index(letter)
        encrypt_index = index + shift_amount
        #index = index % len(alphabet)-1
        if encrypt_index > len(alphabet)-1:
            #index -= len(alphabet)
            encrypt_index = encrypt_index % len(alphabet)
        encrypted_text += alphabet[encrypt_index]
    print(f"The encoded text is {encrypted_text}")

def decrypt(encrypt_text, shift_amount):
    plain_text = ""
    for letter in encrypt_text:
        index = alphabet.index(letter)
        decrypt_index = index - shift_amount
        if decrypt_index < 0:
            decrypt_index = decrypt_index % len(alphabet)
        plain_text += alphabet[decrypt_index]
    print(f"The decoded text is {plain_text}")
  
if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction == "decode":
    decrypt(encrypt_text=text, shift_amount=shift) """



