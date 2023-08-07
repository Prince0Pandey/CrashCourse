
guest_list = ['satyam','hemant','arun','roshan']
print("01",guest_list,"\n")
print(f"Hii {guest_list[0].title()}, Would you like to meet at Dinner Today!")
print(f"Hii {guest_list[1].title()}, Would you like to meet at Dinner Today!")
print(f"Hii {guest_list[2].title()}, Would you like to meet at Dinner Today!")
print(f"Hii {guest_list[3].title()}, Would you like to meet at Dinner Today!\n")
busy = guest_list.pop()
print(f"{busy} will not be able to come to dinner.\n")
guest_list.append('Mrunali')
print(guest_list,"\n")

print(f"Hii {guest_list[0].title()}, Would you like to meet at Dinner Today!")
print(f"Hii {guest_list[1].title()}, Would you like to meet at Dinner Today!")
print(f"Hii {guest_list[2].title()}, Would you like to meet at Dinner Today!")
print(f"Hii {guest_list[3].title()}, Would you like to meet at Dinner Today!\n")