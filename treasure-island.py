print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#create first prompt, make any input lowercase
leftright = input('You come to a fork in the road.  Do you go left or right? ').lower()
if leftright == 'left':
  #second prompt, make any input lowercase
  swimwait = input('You come to a river.  Do you swim or wait? ').lower()
  if swimwait == 'wait':
    #third prompt, make any input lowercase
    doors = input('After getting off the boat, you find a passageway in the cliffs with three doors.  Which door do you choose?  Blue, yellow, or red? ').lower()
    #doors outcomes
    if doors == 'yellow':
      print('You find a treasure chest in the room.  The chest is empty, but you\'re not dead.  You win!')
    elif doors == 'blue':
      print('You walk into a room full of hungry lions.  Game over.')
    else:
      print('There were explosives rigged to explode when the door opens.  Game over.')
  #swim outcome
  else:
   print('You drown in the current.  Game over.') 
  #go right outcome
  else:
  print('You fell into a spike pit.  Game over.')
