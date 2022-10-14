import random
import os
import blackjack_art

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Calculates score of cards in a list"""
  #checking for blackjack (2 cards totaling 21)
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_total, computer_total):
  """Compare the hands to determine a winner"""
  if user_total == 0 and computer_total == 0:
    return "     Dealer has Blackjack. Dealer wins."
  if user_total == 0:
    return "     You have Blackjack!  You win!"
  elif computer_total == 0:
    return "     Dealer has Blackjack.  You lose."
  elif user_total > 21:
    return "     You bust.  Dealer wins."
  elif computer_total > 21:
    return "     Dealer bust!  You win!"
  elif user_total == computer_total:
    return "     It's a draw."
  elif user_total > computer_total:
    return "     You win!"
  else:
    return "     Dealer wins."

def play_game():
  """Play Blackjack!"""
  user_cards = []
  computer_cards = []
  in_progress = True
  print(blackjack_art.logo)
  for int in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  print(f"      Dealer's first card:  {computer_cards[0]}")
  
  while in_progress:
    #check scores and print hands
    user_total = calculate_score(user_cards)
    computer_total = calculate_score(computer_cards)
    print(f"Your cards:  {user_cards} , current score:  {user_total}")
    #check for blackjack/bust
    if user_total == 0 or computer_total == 0 or user_total > 21 or user_total == 21:
      in_progress = False
      compare(user_total, computer_total)
    else:
      #ask if user wants another card, recalc total, reprint
      user_hit = input("Would you like another card?  'Yes' or 'No'. ").lower()
      if user_hit == 'yes':
        user_cards.append(deal_card())
        user_total = calculate_score(user_cards)
      else:
        in_progress = False
      #when user is done drawing cards, computer draws as long as no blackjack and less than or equal to 17
  while computer_total != 0 and computer_total <= 17 and user_total != 0 and user_total < 21:
    print("     Dealer hits.")
    computer_cards.append(deal_card())
    computer_total = calculate_score(computer_cards)
  #after computer draws cards, print hand, score
  print(f"Dealer's hand: {computer_cards} , Dealer's score: {computer_total}")
  #print results
  print(compare(user_total, computer_total)) 
      
while input("Would you like to play Blackjack?  Please type 'yes' or 'no'.  ").lower() == "yes":
  os.system('clear')
  play_game()
