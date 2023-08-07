#list comprehension
cubes = [value**3 for value in range(1,11)]
for i in range(1,11):
    print(f"the cube of {i}: {cubes[i-1]}.")