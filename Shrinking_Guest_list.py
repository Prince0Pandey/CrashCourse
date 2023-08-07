
guest_list = ['satyam','hemant','arun','roshan']
print("01",guest_list,"\n")

print("Hello everyone, I found a bigger dinner table")
guest_list.insert(0,'Mrunali')
guest_list.insert(2,'divya')
guest_list.append('sanskruti')

print(f"Hii {guest_list[0].title()}, Would you like to meet at Dinner Today")
print(f"Hii {guest_list[1].title()}, Would you like to meet at Dinner Today")
print(f"Hii {guest_list[2].title()}, Would you like to meet at Dinner Today")
print(f"Hii {guest_list[3].title()}, Would you like to meet at Dinner Today")
print(f"Hii {guest_list[4].title()}, Would you like to meet at Dinner Today")
print(f"Hii {guest_list[5].title()}, Would you like to meet at Dinner Today")
print(f"Hii {guest_list[6].title()}, Would you like to meet at Dinner Today\n")

print(guest_list,"\n")
print("I can invite only two people for dinner.")

removed_person = guest_list.pop()
print(f"Sorry {removed_person}, I can't invite you to dinner")
removed_person = guest_list.pop(2)
print(f"Sorry {removed_person}, I can't invite you to dinner")
removed_person = guest_list.pop(2)
print(f"Sorry {removed_person}, I can't invite you to dinner")
removed_person = guest_list.pop(0)
print(f"Sorry {removed_person}, I can't invite you to dinner")
removed_person = guest_list.pop(1)
print(f"Sorry {removed_person}, I can't invite you to dinner\n")

print(guest_list)

print(f"Hii {guest_list[0].title()}, You are still invited for Dinner Today")
print(f"Hii {guest_list[1].title()}, You are still invited for Dinner Today")
del guest_list[0]
del guest_list[0]
print(guest_list)