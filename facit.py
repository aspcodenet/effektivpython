import string
import random
import timeit

ANTAL_BILAR = 10_000_000

class Car:
    def __init__(self, reg:str):
        self.reg = reg

    def __str__(self):
        return self.reg

def generate_reg() -> str:
    reg = ""
    for _ in range(3):
        reg += random.choice(string.ascii_uppercase)

    for _ in range(3):
        reg += random.choice(string.digits)

    return reg

cars:list[Car] = []

# print(generate_reg())

for car in range(ANTAL_BILAR):
    new_reg = generate_reg()
    new_car = Car(new_reg)
    cars.append(new_car)

    # cars.append(Car(generate_reg()))

for car in cars[:20]:
    print(car)

def get_car_by_reg(cars:list[Car], reg:str) -> bool:
    for car in cars:
        if car.reg == reg:
            return True
    return False

car_1000 = cars[1000].reg
car_1000000 = cars[ANTAL_BILAR - 1].reg

start = timeit.default_timer()
get_car_by_reg(cars, car_1000)
end = timeit.default_timer()

print(f"Tog {(end-start)*1000} ms att hitta bil på 1000:e plats")


start = timeit.default_timer()
get_car_by_reg(cars, car_1000000)
end = timeit.default_timer()

print(f"Tog {(end-start)*1000} ms att hitta bil på 1000000:e plats")


####### IMPROVEMENT ########

dict_cars:dict[str,list[Car]] = {}

for bokstav in string.ascii_uppercase:
    dict_cars[bokstav] = []

for car in cars:
    dict_cars[car.reg[0]].append(car)

def get_car_by_reg_dict_version(cars:dict[str,list[Car]], reg:str) -> bool:
    list_to_search = cars[reg[0]]
    return get_car_by_reg(list_to_search, reg)

start = timeit.default_timer()
get_car_by_reg_dict_version(dict_cars, car_1000)
end = timeit.default_timer()

print(f"Tog {(end-start)*1000} ms att hitta bil på 1000:e plats i dict-versionen")


start = timeit.default_timer()
get_car_by_reg_dict_version(dict_cars, car_1000000)
end = timeit.default_timer()

print(f"Tog {(end-start)*1000} ms att hitta bil på 1000000:e plats i dict-versionen")


############# USE SEARCH ############################# 

sorted_cars = cars.copy()

sorted_cars.sort(key=lambda x:x.reg)

def get_car_by_reg_sorted_list(cars:list[Car], reg:str) -> bool:
    for car in cars:
        if car.reg == reg:
            return True
        elif car.reg > reg:
            return False
    
    return False

start = timeit.default_timer()
get_car_by_reg_sorted_list(sorted_cars, car_1000)
end = timeit.default_timer()

print(f"Tog {(end-start)*1000} ms att hitta bil på 1000:e plats i sorted-versionen")


start = timeit.default_timer()
get_car_by_reg_sorted_list(sorted_cars, car_1000000)
end = timeit.default_timer()


print(f"Tog {(end-start)*1000} ms att hitta bil på 1000000:e plats i sorted-versionen")

############ Biniary-Search #######################

def bin_search_cars_by_reg(cars:list[Car], reg:str) -> bool:
    start = 0
    end = len(cars) - 1 


    while start <= end:
        mid = (start + end)//2

        if cars[mid].reg == reg: 
            return True
        
        elif cars[mid].reg < reg:
            start = mid + 1

        else:
            end = mid - 1

    return False

start = timeit.default_timer()
bin_search_cars_by_reg(sorted_cars, car_1000)
end = timeit.default_timer()

print(f"Tog {(end-start)*1000} ms att hitta bil på 1000:e plats i binsearch-versionen")


start = timeit.default_timer()
bin_search_cars_by_reg(sorted_cars, car_1000000)
end = timeit.default_timer()
       
print(f"Tog {(end-start)*1000} ms att hitta bil på 1000000:e plats i binsearch-versionen")