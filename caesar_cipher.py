import caesar_art
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#define encode/decode function
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  #if decode, make shift negative
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #check to see if character is alphabetic.  if yes, encode.  if not, add unaltered char to string. 
    if char.isalpha():
      position = alphabet.index(char)
      new_position = position + shift_amount
      #prevent out of bounds error.  if original letter towards end of alphabet, move to start of list.
      if new_position > 25:
        new_position -= 26
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result:\n{end_text}")
  print("Please save result as screen will clear upon restart or exit.")

print(caesar-art.logo)

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  #input validation.  will not accept answers other than encode or decode for direction. 
  if direction == 'encode' or direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    #account for shift number greater than 25
    if shift > 25:
      shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    #ask if user wants to restart after running through function
    result = input("Type 'yes' to restart, 'no' to exit.\n").lower()
    if result == 'yes':
      #keep the screen uncluttered
      os.system('clear')
      print(caesar-art.logo)
    else:
      should_continue = False
      os.system('clear')
      print('Goodbye.')
  else:
    os.system('clear')
    print(caesar-art.logo)
    print("Invalid Input.")
