import os
import random
import art
import game_data

def random_account():
  """Choose a random account from data in game_data.py"""
  person = random.choice(game_data.data)
  return person

def more_followers():
  """Determine which account has more followers"""
  a = account_a["follower_count"]
  b = account_b["follower_count"]
  if a > b:
    return account_a
  else:
    return account_b

def check_guess(user_guess, winner, user_score):
  if user_guess == 'A':
    user_guess = account_a
  else:
    user_guess = account_b
  if user_guess == winner:
    user_score += 1
    return user_score
  else:
    print(f"\nGame over.  You scored {user_score} points!")
    return False
    
#create empty dictionaries to hold entries from random choices
account_a = {}
account_b = {}
#set variable for user score
user_score = 0
#Choose account a 
account_a = random_account()

can_play = True
while can_play:
  #Choose account b
  account_b = random_account()
  #Display comparison
  print(art.logo)
  print(f"\nYou have {user_score} points!")
  print(f"\nCompare A: {account_a['name']}, {account_a['description']}, from {account_a['country']}.")
  print(art.vs)
  print(f"\nCompare B: {account_b['name']}, {account_b['description']}, from {account_b['country']}.")
  #Determine who has more followers
  winner = more_followers()
  #Ask user to guess who has more followers and check guess
  user_guess = input("\nWho do you think has more followers?  Type 'A' or 'B': ")
  user_score = check_guess(user_guess, winner, user_score)
  if user_score == False:
    can_play = False
  else:
    account_a = winner
    os.system("clear")
