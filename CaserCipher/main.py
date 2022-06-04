alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '?', '"', '$', "'"]

# from: https://www.adamsmith.haus/python/answers/how-to-check-if-an-index-exists-in-a-list-in-python

def codec(direction_local, text, shift):
  cipher_text=" "
  length = len(text)
  for i in range(0,length):
    if  text[i] not in alphabet :
      cipher_text += text[i]
    else:
      old_index = alphabet.index(text[i])
      if (direction_local == 'encode' ):
        new_index = (old_index + shift) % 42
      elif(direction_local == 'decode'):
        temp_index = old_index - shift
        if (temp_index < 0 ):
          temp_index = temp_index + 42
        new_index = temp_index % 42
      cipher_text += alphabet[new_index]
  print(f"The {direction_local} text is: {cipher_text}")

# Main
# check input first.
from art import logo
print(logo)
ans =" "
while (ans != "no"):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if (direction.isalpha()) and (direction == 'encode') or (direction == 'decode'):
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    codec(direction, text, shift)
  else:
    print("Invalid input")
  ans = input ("Would you like to try again? ").lower()


