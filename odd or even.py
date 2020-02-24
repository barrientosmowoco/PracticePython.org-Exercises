#
# Exercise #2
#
# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
#       Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#       1. If the number is a multiple of 4, print out a different message.
#       2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#          If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
#
# Problem found here: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#


def odd_or_even():
    number_to_check = input('Type a number to check if it is even or odd: ')
    number_to_divide_by = input('Type a number to divide by: ')

    odd_or_even_ans = int(number_to_check) % 2
    multiple_of_4 = int(number_to_check) % 4

    divided = int(number_to_check) % int(number_to_divide_by)

    if odd_or_even_ans == 1:
        print("Your number is odd.")
    else:
        print("Your number is even.")

    if multiple_of_4 == 0:
        print("Its a multiple of 4")

    if divided == 0:
        print("Your number you wanted to check if its even or odd IS divisible by the 2nd number you imputed")
    else:
        print("Your number you wanted to check if its even or odd is NOT divisible by the 2nd number you imputed")


if __name__ == '__main__':
    odd_or_even()
