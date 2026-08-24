# class Player:
#     def __init__(self, name, birthyear):
#         self.name = name
#         self.birthyear = birthyear

# p1 = Player("John", 1990)
# p2 = Player("Alice", 1995)
# p3 = Player("Bob", 1985)
# p4 = Player("Anders", 2000)

# list_of_players = [p1, p2, p3, p4]

#         # VAD
# # newList = [player for player in list_of_players if player.name.startswith("A")]
# # for player in newList:
# #     print(player.name, player.birthyear)
# newList = [2026-player.birthyear for player in list_of_players if player.name.startswith("A")]
# for age in newList:
#     print(age)




# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = []

# for fruitName in fruits:
#     if "a" in fruitName:
#         newlist.append(fruitName)


# // SELECT fruitName, price * 1.25 FROM fruits WHERE fruitName LIKE '%a%'

# //                                    tabellen  WHERE delen(filter)
# newlist = [len(fruitName) for fruitName in fruits if "a" in fruitName]

# print(newlist)