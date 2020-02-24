#
# Exercise #1
#
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Problem found here: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#

import datetime


def character_input():
    name = input('Type your name: ')
    year = input('Type your age: ')

    current_year = datetime.date.today().year

    year_they_turn_100 = current_year - int(year) + 100

    answer = name + ', you will turn 100 in ' + str(year_they_turn_100)
    print(answer)


if __name__ == '__main__':
    character_input()
