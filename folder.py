
title=('Number guessing game')
print(title)
title2=('Guess a number (between 1 to 9)')
print(title2)

guess= int(input('Enter your guess'))
if (guess<7):
    print('Your guess was too low : guess a number higher than ',guess )
   
elif (guess>7):
     print('Your guess was too low : guess a number lower than ',guess )
    
else : 
       print('Congratulations ! You Won!!' )
       
