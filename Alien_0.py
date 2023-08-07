alien_0 = {'color' : 'green', 'points' : 5,}

new_point = alien_0['points']                   # storing value of point in new variable
print(f"you just earned {new_point} points.")   # printing the value of new variable.
print(f"the alien is {alien_0['color']} in color.\n")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(f"Original position: {alien_0['x_position']}.")

# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    # This must be a fast alien
    x_increment = 3

# New position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}.\n")
print(f"Before deleting the 'point':\n{alien_0},")

# Deleting key-value from dictionary
del alien_0['points']
print(f"After deleting the 'point':\n{alien_0},")