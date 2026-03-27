# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.

# The program should handle the following exceptions:

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.
def sum_numbers_from_file():
    ######################
    with open("numbers.txt", "r") as f:
        total = sum(int(line) for line in f if line.strip())
        print (f'the sum of the file is {total}')
    
    try:
        with open("numbers.txt", "r") as f:
            total = sum(int(line) for line in f if line.strip())
            for line in f:
                line = line.strip
                if not line:
                    continue
                try:
                    total = sum(int(line) for line in f if line.strip())
                except ValueError:
                    print (f'{line.strip} is not a valid number')
    except IOError:
        print ('file not found')
    ######################


# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()