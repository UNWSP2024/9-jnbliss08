# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

import random

def make_random_numbers():
    random_number = random.randint(1, 500)
    return random_number

def get_number_of_numbers():
    number_of_numbers = input('how many numbers do you want? ')
    while int(number_of_numbers) > 1000:
        print('please enter a number between 1 and 1000')
        number_of_numbers = input('how many numbers do you want? ')
    while int(number_of_numbers) < 1:
        print('please enter a number between 1 and 1000')
        number_of_numbers = input('how many numbers do you want? ')
    return int(number_of_numbers)

def main():
    with open('random_numbers.txt', 'w') as file:
        number_of_numbers = get_number_of_numbers()
        for i in range(number_of_numbers):
            random_number = make_random_numbers()
            file.write(str(random_number))
            file.write('\n')

main()



















