# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def guessNum(x):
    randomVal = random.randint(1, x)
    #print(randomVal)
    guess = 0
    while guess != randomVal:
        guess = int(input(f'try again with new number from 1 to {x}: '))
        if guess < randomVal:
            print(f'Guess something higher than {guess}')
        elif guess == randomVal:
            print('Congratulations Sherlock Homes! you got it')
        else:
            print(f'Guess something lower than {guess}')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    guessNum(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
