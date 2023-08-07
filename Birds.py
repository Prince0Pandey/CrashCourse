
birds = ['peacock','parrot','pigeon','eagle','owl']     # creating a list of birds
print("01",birds)                                       # printing list
birds.append('dove')                                    # add element at the end
print("02",birds)                                       # printing list
print(birds[-1].upper())                                # printing a particular value of the list with -ve index value
birds.insert(4,'hen')                                   # inserting value with the help of insert function
print("03",birds)                                       # printing list
del birds[5]                                            # removing a element from a list using del statement
print("04",birds)                                       # printing list
birds.pop()                                             # popping a element
print("05",birds)                                       # printing list
popped_birds = birds.pop()                              # storing the value that popped
print(popped_birds)                                     # printing value of the popped element
print("06",birds)                                       # printing list
last_bird = birds.pop()                                 # storing the value that is to be popped
print(f"last bird that i had was {last_bird}.")         # printing last popped
print("07",birds)                                       # printing list
first_bird = birds.pop(0).title()                       # storing the value that is to be popped
print(f"First bird that i had was {first_bird}.")       # printing the message and value that is to be pop
print("08",birds)                                       # printing list
birds.remove('parrot')                                  # removing the value using remove method
print("09",birds)                                       # printing list
toMuchCare = 'pigeon'                                   # storing the element into variable that is to be pop
birds.remove(toMuchCare)                                # removing the element
print(f"A {toMuchCare.title()} needs to much care")     # printing the message and value that is to be removed
print("10",birds)                                       # printing list