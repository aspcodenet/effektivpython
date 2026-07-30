import random

elever = [
    "Elie",
    "Fatmeh",
    "Ahmad",
    "Ali",
    "Anton",
    "August",
    "David",
    "Emanuel",
    "Tia",
    "Hampus",
    "Andreas",
    "Viktor",
    "Kevin",
    "Amin",
    "Rasmus",
    "Gustav"
]

random.shuffle(elever)

grupper = []

for i in range(4):
    start = i*4
    grupper.append(elever[start:start+4])

for gruppnummer, grupp in enumerate(grupper, start=1):
    print(f"Grupp{gruppnummer}")
    for elev in grupp:
        print(f"\t-{elev}")