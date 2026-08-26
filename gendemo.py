import random
import string
from time import sleep  
class Car:
    def __init__(self, reg:str):
        self.reg = reg

    def __str__(self):
        return f"Car with registration: {self.reg}"

# skapa bilar
# def readCarsFromFile():
#     list_of_cars = []
#     for i in range(1000000):
#         # slumpa fram ett regnummer
#         registration_number = ""
#         for _ in range(3):
#             registration_number += random.choice(string.ascii_uppercase)
#         for _ in range(3):
#             registration_number += random.choice(string.digits)

#         list_of_cars.append(Car(registration_number))
#         sleep(3)
#     return list_of_cars

# skapa bilar med en generator
def readCarsFromFile():
    for i in range(1000000):
        # slumpa fram ett regnummer
        registration_number = ""
        for _ in range(3):
            registration_number += random.choice(string.ascii_uppercase)
        for _ in range(3):
            registration_number += random.choice(string.digits)

        sleep(3)
        yield Car(registration_number)
 



#listcars = readCarsFromFile()
# helA LISTAN måsyte vara klar innan vi kommer hit
for x in readCarsFromFile():
    print(x)

# lista = [0,1,2,3,4]

# # SKILLNAD???
# print("Alla tal sätt 1")
# for i in [0,1,2,3,4]:
#     print(i)

# print("Alla tal sätt 2")
# # iterator kan man bara jobba med från börjAN TILL SLUT
# for i in range(5):
#     print(i)
