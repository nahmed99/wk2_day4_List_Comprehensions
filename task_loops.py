# using a single list comprehension 
# - return a list of only odd ages

ages = [5, 15, 64, 27, 84, 26]

odd_ages = [age for age in ages if age % 2 != 0] 
print(odd_ages)



# TASK 2:
chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
# Return a new list with chickens whose name is more than 10 characters
# Return a list of chickens whose name stars with the letter H

long_names = [chicken for chicken in chicken_names if len(chicken) > 10] 
print(long_names)


start_names_H = [chicken for chicken in chicken_names if chicken[0] == 'H'] 
print(start_names_H)

