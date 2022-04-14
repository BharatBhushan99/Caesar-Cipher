import graphics

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):

  message=""

  for letter in text:

    if letter in alphabet:
      current_index = alphabet.index(letter)
    
      if direction == 'encode':
        new_index = current_index + shift
    
        if new_index > 25:
          new_index = (new_index % 25) - 1
    
      elif direction == 'decode':
        new_index = current_index - shift
    
      letter = alphabet[new_index]
   
    message += letter
      
  print(f"Here's your {direction}d result: {message}")
  
keepLooping = True

print(graphics.logo)

while keepLooping:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  message = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))

  caesar(message, shift, direction)

  choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if choice == 'no':
    keepLooping = False
    print("Goodbye")
