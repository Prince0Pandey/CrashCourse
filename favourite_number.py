favourite_number = {
    'satyam' : [12,23,34,45,56,67],
    'roshan' : [78,89,90,11,22,43],
    'prince' : [45,56,74,36,89,90],
}
for name,fav_number in favourite_number.items():
    print(f"{name.title()}'s favorite numbers:\n\t{fav_number}.")