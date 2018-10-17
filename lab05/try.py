"""
A simple application to show off try-except

Author: Walker M. White
Date:   September 6, 2017 (Python 3 Version)
"""

if __name__ == '__main__':
    try:
        input = input('Number: ')     # get number from user
        x = float(input)                  # convert string to float
        print('The next number is '+str(x+1))
    except:
        print('Hey! That is not a number!')
    print('Program is done')
