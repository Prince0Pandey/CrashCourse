my_pizza = ['pizza01','pizza02','pizza03','pizza04']
friends_pizza = my_pizza[:]
print(f"my Pizza List: {my_pizza}")
print(f"my Friends Pizza List: {friends_pizza}")

my_pizza.append('pizza05')
my_pizza.append('pizza06')

friends_pizza.append('pizza07')
friends_pizza.append('pizza08')

print("\nmy Pizza List:")
for pizza in my_pizza:
    print(pizza)

print("my Friends Pizza List:")
for pizza in friends_pizza:
    print(pizza)