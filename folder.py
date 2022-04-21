
import random 
title=('Number guessing game')
print(title)
number=random.randint(1,9)
chances=0
while chances<5:
     title2=('Guess a number (between 1 to 9)')
     print(title2)

     guess= int(input('Enter your guess'))
     if (guess<number):
         print('Your guess was too low : guess a number higher than ',guess )
   
     elif (guess>number):
           print('Your guess was too low : guess a number lower than ',guess )
    
     else : 
           print('Congratulations ! You Won!!' )
           break 
     chances=chances+1
       
