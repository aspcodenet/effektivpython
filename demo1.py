import random
import string
import time

class Car:
    def __init__(self, reg:str):
        self.reg = reg

    def __str__(self):
        return f"Car with registration: {self.reg}"


list_of_cars = []

for i in range(10000000):
    # slumpa fram ett regnummer
    registration_number = ""
    for _ in range(3):
        registration_number += random.choice(string.ascii_uppercase)
    for _ in range(3):
        registration_number += random.choice(string.digits)

    list_of_cars.append(Car(registration_number))



def get_car_by_reg(cars:list[Car], reg:str) -> bool:
    for car in cars:
        if car.reg == reg:
            return 
    return False


for car in list_of_cars[:20]:
    print(car)


# Hitta en bil med ett specifikt regnummer
lastRegno = list_of_cars[-1].reg
place10000 = list_of_cars[10000].reg

print(f"Last registration number: {lastRegno}")
print(f"Registration number at position 10000: {place10000}")


# Measure time taken to find the car with the last registration number

start_time = time.time()
found = get_car_by_reg(list_of_cars, lastRegno)
end_time = time.time()
print(f"Time taken to find car with last registration number: {end_time - start_time}")

# Measure time taken to find the car with the registration number at position 10000
start_time = time.time()
found = get_car_by_reg(list_of_cars, place10000)
end_time = time.time()
print(f"Time taken to find car with registration number at position 10000: {end_time - start_time}")



