import csv
import os

FILNAMN = "hockeyplayers.csv"

class Player:
    def __init__(self, id,namn,teamname,games,goals,ass,positions):
        self.id = id
        self.namn = namn
        self.teamname = teamname
        self.games = games
        self.goals = goals
        self.ass = ass
        self.positions = positions


def read_csv_file()-> list[Player]:
    if not os.path.exists(FILNAMN):
        print(f"Filen '{FILNAMN}' hittades inte.")
        return []
    with open(FILNAMN, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            Player(
                 row["id"],
                 row["namn"],
                 row["teamname"],
                 int(row["games"]),
                 int(row["goals"]),
                 int(row["ass"]),
                 row["position"]
             )
            for row in csv.DictReader(f)
        ]

        #players = []
        # for row in reader:
        #     player = Player(
        #         row["id"],
        #         row["namn"],
        #         row["teamname"],
        #         int(row["games"]),
        #         int(row["goals"]),
        #         int(row["ass"]),
        #         row["position"]
        #     )
        #     players.append(player)
        # return players

def filterPlayersWithGoals(players, min_goals):
    return [player for player in players if player.goals > min_goals]
    
    # list = []
    # for player in players:
    #     if player.goals > min_goals:
    #         list.append(player)
    # return list

players = []
while True:
    print("1. Läs in hockeyspelare från CSV-fil")
    print("2. Visa alla hockeyspelare")
    print("3. Visa hockeyspelare med fler än X mål")
    input_choice = input("Välj ett alternativ (1-3) eller 'q' för att avsluta: ")
    if input_choice == "1":
        players = read_csv_file()
        print(f"{len(players)} hockeyspelare har lästs in från filen.")
    elif input_choice == "2":
        for player in players:
            print(player.namn)
    elif input_choice == "3":
        goals = int(input("Ange minsta antal mål: "))
        #filtered_players = [player for player in players if player.goals > goals]
        filtered_players = filterPlayersWithGoals(players, goals)
        for player in filtered_players:
            print(f"{player.namn} - Mål: {player.goals}")
