def madLibs():
    adj = input('Your adjective here:')
    verbVal = input('Your action verb:')
    timeVal = input('Your target time here:')

    madLibVal = f"MadLib is fun im so {adj} to start these projects I hope I will be able to {verbVal} all the projects in {timeVal}"
    print(madLibVal)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    madLibs()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
