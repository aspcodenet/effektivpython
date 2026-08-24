tal = [3, 6, 9, 12, 15]

nyaTal = []
for t in tal:
    if t % 2 == 0:
        nyaTal.append(t*2)
    else:
        nyaTal.append(t*3)

def twoOrThree(t):
    if t % 2 == 0:
        return t*2
    else:
        return t*3

nyaTal = [twoOrThree(t) for t in tal]


# firstLettersLisif t = []
# allWords = ["Python","is", "fun"]

# for word in allWords:
#     firstLettersList.append(word[0])

# print(firstLettersList)

allWords = ["Python","is", "fun"]
firstLettersList = [word[0] for word in allWords]
# DET FÖRSTA ÄR VAD VI VILL HA, DET ANDRA ÄR VARIFRÅN VI HÄMTAR DET



ordLista = ["apple", "banana", "cherry", "date"]
nyaord = [ord for ord in ordLista if "a" in ord]
for ord in nyaord:
    print(ord)






listan = [i for i in range(20) if i % 2 == 0]
for i in listan:
    print(i)


list = []
for i in range(20):
    if i % 2 == 0:
        list.append(i)


for i in list:
    print(i)
