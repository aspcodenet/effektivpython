import random

# class är ingenting - template - ritning
# OOP = object oriented programming - tänk substantiv
class Person:
    def __init__(self, name: str, age: int): # mandatory
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        else:
            self.__age = age



    def act(self):
        actions = ["eats", "drinks", "burps"]
        action = random.choice(actions)
        print(f"{self.name} {action}.")

    def might_level_up(self):
        pass


stefan = Person("Stefan", 54)
#age = int(input("Enter a new age for Stefan: "))

#stefan.age = age

kerstin = Person("Kerstin", 53)
oliver = Person("Oliver", 18)
josefine = Person("Josefine", 23)
player_list = [stefan, kerstin, oliver, josefine]


while True:
    for player in player_list:
        player.act()
        player.might_level_up()
    input("Press Enter to continue to the next round...")
