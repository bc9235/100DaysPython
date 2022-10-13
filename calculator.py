import calc_art
import os

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

#create dictionary of operations
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(calc_art.logo)
  #ask user for first number and print operations symbols
  num1 = float(input("What's the first number? "))
  for symbol in operations:
    print(symbol)
  #establish condition to continue calculating
  do_calc = True
  while do_calc:
    op_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))
    #use inputs to call and execute appropriate function
    answer = operations[op_symbol](num1, num2)
    print(f"{num1} {op_symbol} {num2} = {answer}")
    #ask if user wants to perform more operations on result or exit, if yes, num1 is now answer
    go_again = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit: ").lower()
    if go_again == 'y':
      num1 = answer
    #if exit, clear screen and reload calculator
    else:
      do_calc = False
      os.system('clear')
      calculator()

calculator()
