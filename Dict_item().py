favorite_language = {
    'roshan' : 'python',
    'satyam' : 'java',
    'arun' : 'javascript',
    'prince' : 'C'
}

# Looping through all key_value pairs using item()
for name, language in favorite_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through keys
for name in favorite_language.keys():               # for name in favorite_language:(by default returns key)
    print(F"Name : {name.title()}.")
print("\n")
friends = ['roshan','satyam']
for name in favorite_language.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_language[name]
        print(f"\t {name.title()}, i see you love {language}!")

