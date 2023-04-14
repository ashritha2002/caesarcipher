alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art 
print(art.logo)

def ceasar(txt,shft,direct):
  ans = ""
  for i in range(0,len(txt)):
    
    if txt[i] in alphabet:
      indx=alphabet.index(txt[i])
      if direct == "encode":
        ans += alphabet[(indx+shift)%26]
      if direct == "decode":
        ans += alphabet[(indx-shift)%26]
    else:
      ans+=txt[i]
  print(ans)

repeat = "yes"

while repeat == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  ceasar(text,shift,direction)
  repeat= input("Type 'yes' if you want to goahead otherwise type 'no':\n")

if repeat == "no":
  print("good bye")

# def encrypt(txt,sft):
#   cipher_text = ""
#   for i in range(0,len(txt)):
#     indx=alphabet.index(txt[i])
#     cipher_text += alphabet[(indx+shift)%26]
#   print(cipher_text)


# def decrypt(txt,sft):
#   plain_text = ""
#   for i in range(0,len(txt)):
#     indx=alphabet.index(txt[i])
#     plain_text += alphabet[(indx-shift)%26]
#   print(plain_text)




# ceasar(text,shift,direction)

