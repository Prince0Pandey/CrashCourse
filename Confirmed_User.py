unconfirmed_users = ['roshan','satyam','prince','arun','mrunali','hemant']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"verifying current user:{current_users.title()}")
    confirmed_users.append(current_users)
print(confirmed_users)