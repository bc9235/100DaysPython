#loop through numbers in range 1 to 100
for num in range(1, 100 + 1):
    #if num is evenly divisible by BOTH 3 and 5, FizzBuzz
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    #if num evenly divisible by 3, Fizz
    elif num % 3 == 0:
        print('Fizz')
    #if num evenly divisble by 5, Buzz
    elif num % 5 == 0:
        print('Buzz')
    #otherwise, number    
    else:
        print(num)
