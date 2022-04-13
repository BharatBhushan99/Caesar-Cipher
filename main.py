alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):

  message=""

  for letter in text:
    current_index = alphabet.index(letter)

    if direction == 'encode':
      new_index = current_index + shift

      if new_index > 25:
        new_index = (new_index % 25) - 1

    elif direction == 'decode':
      new_index = current_index - shift

    message += alphabet[new_index]

  print(f"Here's your {direction}d result: {message}")
  
caesar(message, shift, direction)
