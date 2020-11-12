
# array of numbers, using range shortcut
numbers = range(1, 11) # starting at 1, and ending before 11, i.e., 1-10

evens_squared = [] # Will contain [4, 16, 36, 64, 100]

for number in numbers:
    # check if number is even
    if number % 2 == 0:
        # if even, square the number and append to evens_squared
        evens_squared.append(number * number)

print(evens_squared)


# List comprehension allows us to write a single line of code and
# do something powerful with a List while the list is being created.

evens_squared_comp = []