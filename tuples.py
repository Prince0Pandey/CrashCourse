dimensions = (20,30,50)
print(dimensions[0])
print(dimensions[1])
print(dimensions[2])

#LOOPING THROUGH TUPLE

print("\nlooping through tuples!")
for dimension in dimensions:
    print(dimension)

print(f"\nOriginal Dimensions: {dimensions}")
dimensions = (60,70,80)
print(f"\nModified Dimensions: {dimensions}\n")

dimensions[0] = 35      # error: tuple object does not support item assignment
