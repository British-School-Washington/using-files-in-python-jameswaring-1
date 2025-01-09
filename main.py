with open('countries.txt', 'r') as file:
    countries = file.readlines()

countries = [country.strip() for country in countries]

country_count = len(countries)

print(f"There are {country_count} countries listed.")

for country in countries:
    if len(country) < 6:
        print(country)