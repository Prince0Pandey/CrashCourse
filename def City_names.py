def city_country(city,country):
    value = f'"{city}, {country}."\n'
    return value
city1 = city_country('mumbai','india')
print(city1.title())

city2 = city_country('bengaluru','india')
print(city2.title())

city3 = city_country('chennai','india')
print(city3.title())