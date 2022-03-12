'''
--------------------------------------------------
Morse Code Translator
--------------------------------------------------
TODO : None

'''

import string
import sys
from decoded import CODE


def display():
    '''
    Displays the menu
    '''
    print('\n', ''.center(80, '='), sep='\n')
    print('WELCOME TO MORSE CODE TRANSLATOR'.center(80, '-'))
    print(''.center(80, '='))
    print('\n', 'MENU'.center(80, '-'), sep='\n')
    print('1. MORSE CODE TO ENGLISH')
    print('2. ENGLISH TO MORSE CODE')
    print('ELSE : EXIT')


def decode(inp_str: string) -> string:
    '''
    Converts the morse code recieved to english using decoded.py
    '''
    answer = ''
    return answer


def encode(inp_str: string) -> string:
    '''
    Converts the english statement recieved to morse code
    '''
    answer = ''
    return answer


def main():
    '''
    Main function of the program
    '''
    display()
    try:
        choice = int(input('Enter: '))
    except ValueError:
        choice = -1
        input_string = input("Enter the string to be converted : ")
    if choice == 1:
        english = decode(input_string)
        print(english)
    elif choice == 2:
        morse_code = encode(input_string)
        print(morse_code)
    sys.exit('\n' + '!!!PROGRAM ENDED!!!'.center(80, '*') + '\n')


if __name__ == '__main__':
    main()
