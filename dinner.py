import random

# class är ingenting - template - ritning
# OOP = object oriented programming - tänk substantiv
class Person:
    def __init__(self, name: str, age: int): # mandatory
        self.name = name
        self.__age = age
        self.__level = 0
        self.__burps_in_a_row = 0
        self.list_of_actions = []
        # self.latestaction = ""
        # self.nextLatestAction = ""
        # self.nextNextLatestAction = ""

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
        if action == "burps":
            self.__burps_in_a_row += 1
        else:
            self.__burps_in_a_row = 0  # Reset the burp counter if the action is not a burp

    def might_level_up(self):
        # kanske öka och
        if self.__burps_in_a_row == 3:
            print(f"{self.name} has burped 3 times in a row and levels up!")
            self.__level += 1
            self.__burps_in_a_row = 0  # Reset the burp counter after leveling up


stefan = Person("Stefan", 54)
#age = int(input("Enter a new age for Stefan: "))

#stefan.age = age

kerstin = Person("Kerstin", 53)
oliver = Person("Oliver", 18)
josefine = Person("Josefine", 24)
player_list = [stefan, kerstin, oliver, josefine]

# alla börjar med level 0
# om man burps 3 gånger på raken så levelar man upp

while True:
    for player in player_list:
        player.act()
        player.might_level_up()
    input("Press Enter to continue to the next round...")
