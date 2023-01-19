class Country(object):
    system = 'Common system'

    def __init__(self, name, population):
        self.name = name
        self.population = population

    # magic method
    def __str__(self):
        return f'Country: {self.name} with population {self.population}'

    def make_declaration(self, speech):
        return f'{self.name} declare: {speech}'

class Republic(Country):
    pass

congo = Republic('Congo', 5_000_000)

print(congo.population)
print(congo.name)
print(congo)


class Republic(Country):
    system = 'Republic system' # Змінили атрибут классу
    test_new_attr = 'New value'

class Federation(Country):
    system = 'Federation system'

germany = Federation('Germany', 80_000_000)
korea = Republic('Korea', 50_000_000)

print('Germany: ', germany.system, 'Name:', germany.name)
print('Korea: ', korea.system, 'Name:', korea.name)
print(dir(korea))


class Empire(Country):
    # system = 'Empire system'
    def __init__(self, name, population, lifetime):
        super().__init__(name, population)
        self.lifetime = lifetime

    def fail(self):
        declaration = super().make_declaration('We fail!')
        print(declaration)
        print('The end')
        print('¯7_(ツ)_/¯')

some_empire = Empire('Some empire', 300_000_00, 30)
some_empire.fail()

class A():
    pass

class B():
    pass

class C(A, B):
    pass

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())


class Statement:
    pass

class Law(Statement):
    pass

class Union:
    def __init__(self, creation_date: int, countries: list[Country], law: Law):
        self.countries  = countries
        self.law = law
        self.creation_date = creation_date


class Wheel:
    pass

class Vehicle:
    pass

class Ship(Vehicle):
    pass

class Bus(Vehicle):
    def __init__(self, wheels: list[Wheel]):
        self.wheels = wheels


spain = Country('Spain', 44_000_000)
eu_law = Law()
european_union = Union(1956, [germany, spain], eu_law)
european_union2 = Union(1956, [germany, spain], eu_law)
for i, country in enumerate(european_union.countries):
    print(f'Member number: {i+1} country.name: {country.name}')
print(f'Created an union on {european_union.creation_date}')


class Rectangle:
    def __init__(self, length, height):
        self._length = length
        self._height = height

    @property
    def area(self):
        return self._length * self._height

class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size, side_size)

s = Square(3)
print(s.area)
rectangle = Rectangle(2, 4)


class Rectangle:
    def __init__(self, length, height):
        self._length = length
        self._height = height

    @property
    def area(self):
        return self._length * self._height

    # Додаємо resize
    def resize(self, new_length, new_height):
        self._length = new_length
        self._height = new_height


class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size, side_size)


rectangle = Rectangle(2, 4)

rectangle.resize(3, 5)
print(rectangle.area == 15)

square = Square(2) # Проблема
square.resize(3, 5)
print(f'Square area: {square.area}')