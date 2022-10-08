#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#set password to empty string to build on
password = ''
#create loop and set user input as range for # of times to loop through letters 
for char in range(1, nr_letters + 1):
  password += random.choice(letters)
#make another loop for symbols 
for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)
#final loop for numbers 
for int in range(1, nr_numbers + 1):
  password += random.choice(numbers)
print(password)
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#make an empty list to store random choices to shuffle later
passlist = []
#make a loop to pick random letters and store them in the list
for char in range(1, nr_letters + 1):
  passlist += random.choice(letters)
#loop for symbols
for char in range(1, nr_symbols + 1):
  passlist += random.choice(symbols)
#loop for numbers
for int in range(1, nr_numbers + 1):
  passlist += random.choice(numbers)
#shuffle order of password
random.shuffle(passlist)
#loop to add each entry of list to new string
password = ''
for item in passlist:
  password += str(item)
print(password)
