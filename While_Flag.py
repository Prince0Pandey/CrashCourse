prompt = "tell me something and i will repeat."
prompt += "\nenter 'quit' to exit:"
message = ""
while message != 'quit':
    message = input(prompt)
    if message.lower() == 'quit':
        active = False
    else:
        print(message)
    message = message.lower()