# object-oriented programming

# method == function
def normal_method():
    pass


# blueprint, tervrajz, nem konkret
class Person:
    # constructor, peldanyosit
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def say_hello(self, kinek_mutatkozzak_be):
        print(f'Hello {kinek_mutatkozzak_be}')


# instance, peldany, konkret, egyedi dolog
person1 = Person("John", 36)

print(person1.name)
print(person1.age)

person2 = Person("Bela", 40)
person2.name == 'Bela'

person3 = Person("Barnus", 14)
person3.age = 15
person3.say_hello('Johnny')

print(person3)

# information encapsulation, information hiding
class House:
    def __init__(self, meret, ar):
        self.meret = meret
        self.ar = ar

    def ceger(self, ceger_felirat):
        print(f'Ennek a haznak a cegerenek a felirata: {ceger_felirat}')


elso_haz = House(70, 15_000_000)
elso_haz.ceger('Tiszta udvar, rendes haz')


