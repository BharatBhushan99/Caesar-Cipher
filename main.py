alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

def ecncrypt(text, shift):

  encrypted_message = ""
  
  for letter in text:
    current_index = alphabet.index(letter)
    new_index = current_index + shift

    if new_index > 25:
      new_index = (new_index % 25) - 1

    encrypted_message += alphabet[new_index]
    
  print(f"Here's your encrypted result: {encrypted_message}")

def decrypt(text, shift):

  decrypted_message = ""

  for letter in text:
    current_index = alphabet.index(letter)
    new_index = current_index - shift

    decrypted_message += alphabet[new_index]

  print(f"Here's your decrypted message: {decrypted_message}")
  
if direction == 'encode':
  ecncrypt(message, shift)
elif direction == 'decode':
  decrypt(message, shift)
else:
  print("Incorrect input.")
  