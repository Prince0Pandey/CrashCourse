prompt = "enter your age.\nEnter 'quit' to exit:\n"
age = ""
while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("the ticket is free of cost.\n")
        elif age >= 3 and age < 12:
            print("the ticket is $10\n")
        elif age >= 12:
            print("the ticket is $15\n")