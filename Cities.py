cities = {
    'mumbai' : {
        'country' : 'india',
        'population' : '20.9 million',
        'fact' : 'Mumbai is home to multiple UNESCO World Heritage Sites'
    },
    'new york': {
        'country': 'usa',
        'population': '8.8 million',
        'fact': "The city's original name was New Amsterdam."
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': "It is the world's most populous metropolitan area."
    },
    'los angeles': {
        'country': 'usa',
        'population': '3.9 million',
        'fact': 'Los Angeles is the only North American city to have hosted the Olympics twice.'
    }
}
for name,city_info in cities.items():
    print(f"Name of the city is {name.title()}\nInformation of city:\n\t{city_info}\n")