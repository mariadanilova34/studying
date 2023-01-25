# Modify the Country class to include a third instance attribute called capital as a string. Store your new class in a
# script and test it out by adding the following code at the bottom of the script:
# japan = Country('Japan', 140_000_000, 'Tokyo')
# print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")
# The output of your script should be:
#
# Japan population is 140000000 and capital is Tokyo.


class Country:
    # adding custom attributes
    def __init__(self, name: str, population: int, capital: str):
        self.name = name
        self.population = population
        self.capital = capital

    def add_population(self, popnumber: int):
        self.population += popnumber

    def anshluss(self, country):
        self.name += '_'
        self.name += country.name
        self.population = country.population


japan = Country('Japan', 140_000_000, 'Tokyo')
print(f"{japan.name} population is {japan.population} and capital is {japan.capital}.")

japan.add_population(1001)
print(f"{japan.name} population is growed to {japan.population}")

'''
Add increase_population method to country class. This method should take an argument and increase population of the 
country on this number.


Create add method to add two countries together. This method should create another country object with the name of the
two countries combined and population of the two countries added together.

(Optional) Implement previous method with magic method
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina

bosnia_herzegovina.population -> 15_000_000
bosnia_herzegovina.name -> 'Bosnia Herzegovina'
'''


class LesserCountry:
    # adding custom attributes
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, other):
        return LesserCountry(self.name + ' ' + other.name, self.population + other.population)

    def __add__(self, other):
        return LesserCountry(self.name + ' ' + other.name, self.population + other.population)


bosnia = LesserCountry('Bosnia', 10_000_000)
herzegovina = LesserCountry('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(f"{bosnia_herzegovina.name} population is {bosnia_herzegovina.population}")

# optional
bosnia_herzegovina2 = bosnia + herzegovina
print(f"{bosnia_herzegovina2.name} population is {bosnia_herzegovina2.population}")