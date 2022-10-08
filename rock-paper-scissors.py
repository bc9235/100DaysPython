import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#make list of rock paper scissors in that order for corresponding index numbers
choices = [rock, paper, scissors]
#ask user for their choice, cast to int and print choice
user = int(input('What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if user >= 3 or user < 0:
  print('You typed an invalid number.')
else:
  print(choices[user])
  #generate random number for computer choice
  computer = random.randint(0, 2)
  print(f'Computer chooses:\n{choices[computer]}')
  #set outcomes
  #rock vs scissors
  if user == 0 and computer == 2:
    print('You win!')
  elif computer == 0 and user == 2:
    print('You lose.')
  #draw
  elif user == computer:
    print('It\'s a draw.')
  elif user > computer:
    print('You win!')
  elif user < computer:
    print('You lose.')
