rivers = {
    'amazon' : 'peru',
    'yello river' : 'china',
    'nile' : 'egypt'
}
for name,country in rivers.items():
    print(f"{name.title()} runs through {country.title()}.")

for name, country in rivers.items():
    print(f"Name : {name.title()}\tCountry : {country.title()}")
