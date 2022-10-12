import os
import silent-auction-art

print(art.logo)

#set empty dictionary to hold name:bid pairs, bidders to accept name:bid pairs
bids = {}
bidders = True

#define function to determine highest bidder
def winning_bid(bids):
  #set placeholders
  highest_bid = 0
  winner = ''
  #compare bids and decide winner
  for name in bids:
    value = bids[name]
    if value > highest_bid:
      highest_bid = value
      winner = name
  print(f'{winner} wins the auction with a bid of ${highest_bid}.')
  
#gather names and bids
while bidders:
  name = input('What is your name? ')
  amount = int(input('How much do you bid? $'))
  #add name and bid to bids dictionary
  bids[name] = amount
  others = input("Is there anyone else who wants to bid?  Please enter 'yes' or 'no'.\n").lower()
  #validate yes or no for input, stop program if anything else
  if others != 'yes' or others != 'no':
    print('Invalid Input.')
    bidders = False
  #clear screen before next bidder input 
  elif others == 'yes':
    os.system('clear')
  elif others == 'no':
    bidders = False
    #call function to determine winner
    winning_bid(bids)
