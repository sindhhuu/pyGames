# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import numpy as np
import pandas as pd


def guessUserVal(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input (f'Guess is {guess} provide H if you want me to guess higher! provide L if you want me to guess lower if its correct say c :')
        if feedback == 'l' or feedback == 'L':
            high = guess - 1
        elif feedback == 'h' or feedback == 'H':
            low = guess + 1
    print (f'the value is correct {guess}')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    guessUserVal(10)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
