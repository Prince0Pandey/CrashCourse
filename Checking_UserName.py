current_users = ['roshan','Adam','shivaay','hemant','arun','ratnesh','mukesh']

new_users = ['mrunali','divya','Adam','arun','sanskruti']

for user in new_users:
    if user in current_users:
        print("Sorry, entered user name is already taken. enter different user name:")

    else:
        print("User name is available.")