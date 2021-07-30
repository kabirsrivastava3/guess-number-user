'''
Project on guessing of secret number of user by computer using random library.
'''

import random

def guessNumberUser(number):
    lowValue = 1
    highValue = number
    feedbackByUser = ""
    while feedbackByUser != 'c':
        if lowValue != highValue:
            guess = random.randint(lowValue,highValue)
        else:
            guess = lowValue      #This could be highValue because lowValue = highValue
        feedbackByUser = input(f"Is {guess} too high(h), too low(l), or correct(c)?? ").lower()
        if feedbackByUser == 'h':
            highValue = guess - 1
        elif feedbackByUser == 'l':
            lowValue = guess + 1

    print(f"Wow!! Great job!! The Computer guessed your number,{guess}, correctly!")


print("Enter the range of number")
output = int(input())
guessNumberUser(output)

# Test Case
#guessNumberUser(10)
