import csv
import os

class Player:
    def __init__(self, id,namn,teamname,games,goals,ass,positions):
        self.id = id
        self.namn = namn
        self.teamname = teamname
        self.games = games
        self.goals = goals
        self.ass = ass
        self.positions = positions


def readPlayerFromFileGenerator(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield Player(
                row["id"],
                row["namn"],
                row["teamname"],
                int(row["games"]),
                int(row["goals"]),
                int(row["ass"]),
                row["position"]
            )

for player in readPlayerFromFileGenerator("hockeyplayers.csv"):
    print(player.namn, player.goals)




def squareOneToTen():
    for i in range(1, 11):
        yield i * i

def squareOneToTenList():
    list = []
    for i in range(1, 11):
        list.append(i * i)
    return list


def infiniteGenerator():
    i = 1
    while True:
        yield i
        i += 1

for tal in infiniteGenerator():
    print(tal)
    if tal > 10:
        break

for tal in squareOneToTen():
    print(tal)


for tal in squareOneToTenList():
    print(tal)


# while True:
#     print("Stefan är bäst!")
#     a = input("Vill du fortsätta? (j/n): ")
#     if a.lower() != "j":
#         break   
