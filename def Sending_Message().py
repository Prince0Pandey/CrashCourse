
def send_messages(messages):
    for message in messages:
        print((f"Message: {message}"))
        sent_message.append(message)

message_list = ['where are you','talk to you later','thank you','have a nice day']
sent_message = []

send_messages(message_list)
print(f"message list:{message_list}")
print(f"sent message:{sent_message}")