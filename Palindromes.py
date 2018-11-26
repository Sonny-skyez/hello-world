'''
Palindromes - This program will check if the word, number or sentence is a palindrome or not.
Enjoy!

A palindrome is a word, number, phrase, or other sequence of characters
which reads the same backward as forward. Sentence-length palindromes may be written when
allowances are made for adjustments to capital letters, punctuation, and word dividers.

Written: 24.11.2018
Author: Chris Brymer
'''


import time
import textwrap

def delay(sleep):
    # function that delays time by 1 second.
    time.sleep(sleep)

def user_choice():
    # function checking if the input statement is not empty.
    txt = '> Please type word / sentence / number to check: '.rjust(53, '-')
    choice_input = input(txt)

    while choice_input is '':
        print('Choose any words or numbers! Try again.'.rjust(52,'-'))
        choice_input = input(txt)

    choice = choice_input.lower()

    return choice


intro_txt = '''
 /$$$$$$$          /$$ /$$                 /$$                                                     
| $$__  $$        | $$|__/                | $$                                                     
| $$  \ $$/$$$$$$ | $$ /$$ /$$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$$
| $$$$$$$/____  $$| $$| $$| $$__  $$ /$$__  $$ /$$__  $$/$$__  $$| $$_  $$_  $$ /$$__  $$ /$$_____/
| $$____/ /$$$$$$$| $$| $$| $$  \ $$| $$  | $$| $$  \__/ $$  \ $$| $$ \ $$ \ $$| $$$$$$$$|  $$$$$$ 
| $$     /$$__  $$| $$| $$| $$  | $$| $$  | $$| $$     | $$  | $$| $$ | $$ | $$| $$_____/ \____  $$
| $$    |  $$$$$$$| $$| $$| $$  | $$|  $$$$$$$| $$     |  $$$$$$/| $$ | $$ | $$|  $$$$$$$ /$$$$$$$/
|__/     \_______/|__/|__/|__/  |__/ \_______/|__/      \______/ |__/ |__/ |__/ \_______/|_______/ '''


print('\n','Welcome to program:'.center(100))
delay(1)
print(intro_txt,'\n')
delay(1)

choice = user_choice()


while choice:


    symbols = textwrap.wrap(choice,1)
    symbols_copy = symbols.copy()
    symbols_copy.reverse()

    if symbols == symbols_copy:
        print('\n','> This is palindrom :-)'.rjust(52,'-'))
        delay(1)
        print('\n')
        txt_exit = '> Do you want to continue? Y/N '.rjust(53,'-')
        choice_exit = input(txt_exit)

        if choice_exit is 'N' or choice_exit is 'n':
            break
        print('\n')
        choice = user_choice()


    else:
        print('\n','> This is not a palindrom :-('.rjust(52,'-'))
        delay(1)
        print('\n')
        txt_exit = '> Do you want to continue? Y/N '.rjust(53,'-')
        choice_exit = input(txt_exit)

        if choice_exit is 'N' or choice_exit is 'n':
            break
        print('\n')
        choice = user_choice()


print('\n\n','> Thanks for using my awesome program! - author <'.center(100,'-'))