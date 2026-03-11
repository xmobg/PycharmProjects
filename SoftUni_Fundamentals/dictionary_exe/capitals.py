countries = input().split(", ")
capitals = input().split(", ")
#countries_and_capitals = {countries[index]:capitals[index] for index in range(len(countries))}
countries_and_capitals = dict(zip(countries,capitals))
for country,capital in countries_and_capitals.items():
    print(f"{country} -> {capital}")
