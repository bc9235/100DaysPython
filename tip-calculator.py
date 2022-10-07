print('Welcome to the tip calculator.')
#gather variables
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? ')) / 100 #divide by 100 to make decimal to add later
people = int(input('How many people to split the bill? '))
#add tip(1.x) and total_bill
with_tip = bill * (1 + tip)
#divide per person
per_person = round(with_tip / people, 2)
per_person = "{:.2f}".format(per_person)
#print what each person owes
print(f'Each person should pay: ${per_person}')
