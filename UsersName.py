user_name = ['roshan','Admin','shivaay','hemant','run']

if user_name:
    for user in user_name:
        if user == 'Admin':
            print("Hello admin, would you like to see a status report?\n")

        else:
            print(f"Hello {user}, thank you for logging in again.\n")

else:
    print("We need to find some users!")