animals = []
animals.append('dog')
animals.append('cat')
animals.insert(0,'rabbit')
for animal in animals:
    print(animal.title())
print("\n")
animals.sort()
print(animals,"\n")
for animal in animals:
    print(f"A {animal} would make a great pet!")
print("\nAny of these animals would make a great pet!")