
cubes = []
for value in range(1,11):
    value = value**2
    cubes.append(value)
for val in range(1,11):
    print(f"the square of {val}: {cubes[val-1]}.")