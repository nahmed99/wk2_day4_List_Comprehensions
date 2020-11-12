
# array of numbers, using range shortcut
numbers = range(1, 11) # starting at 1, and ending before 11, i.e., 1-10

evens_squared = [] # Will contain [4, 16, 36, 64, 100]

for number in numbers:
    # check if number is even
    if number % 2 == 0:
        # if even, square the number and append to evens_squared
        evens_squared.append(number * number)

print(evens_squared)


#TBH, you probably don't want to do this - not easy to understand unless you are an expert.
#TBH, you probably don't want to do this - not easy to understand unless you are an expert.
#TBH, you probably don't want to do this - not easy to understand unless you are an expert.


# List comprehension allows us to write a single line of code and
# do something powerful with a List while the list is being created.

# syntax is ["output"   "for loop"   "optional conditionals"] - the output variable name needs 
# to be the same as the one used in the for loop.

#evens_squared_comp = [kidda * kidda for kidda in numbers if kidda %2 ==0] # Note the syntax!

# You can use range instead of the number list...
evens_squared_comp = [kidda * kidda for kidda in range(1, 11) if kidda %2 ==0] 
print(evens_squared_comp)