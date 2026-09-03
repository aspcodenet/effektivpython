# funktioner - black box
#     ABSTRACTION
# funktion = ett kodblock med ett namn som kan återanvändas
# funktion behöver inte veta hur den fungerar, bara vad den gör
# funktion behöver inte ha ett namn - LAMBDA
# sort ändrar originalet
# sorted ändrar INTE originalet, utan returnerar en ny lista

words = ["apple", "pie", "banana", "cherry"]


sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words)




from dataclasses import dataclass

@dataclass
class Player:
    Name:str
    Goals: int
    Assists: int

lista = [Player("Stefan",12,22), Player("Mats",11,99), Player("Foppa",10,33), Player("Peter",9,44), Player("Henke",8,55)]

# ta fram en ny lista med spelare som har mer än 10 mål
# motsvarar if i list comphrehensions
newlist = list(filter(lambda p: p.Goals > 10, lista))
print(newlist)

# SELECT goials*10 from A
playersGoals = [p.Goals for p in lista if p.Goals > 10]
print(playersGoals)
playersGoalsWithMap = list(map(lambda p: p.Goals,lista))


# def sortFunc(p):
#     return p.Goals + p.Assists

# lista.sort(key=sortFunc, reverse=True)
lista.sort(key=lambda p: p.Goals + p.Assists, reverse=True)
print(lista)







# går igenom alla filer i en folder och för varje fil i foldern
# kolla om en viss IP address finns i den
def check_ip_in_files(ip_address, folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                if ip_address in content:
                    print(f"IP address {ip_address} found in {filename}")


# går igenom alla filer i en folder och för varje fil i foldern
# kolla om en texten "deposit" finns i den
def check_deposit_in_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                if "deposit" in content:
                    print(f"Text 'deposit' found in {filename}")


def scan_all_files(folder_path, func):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                func(content)  # Call the provided function with the file content

def checkip(line:str):
    if "12.12.12.12" in line:
        print("IP found in line:", line)

def checkdeposit(line:str):
    if "deposit" in line:
        print("Deposit found in line:", line)

scan_all_files("/path/to/folder", checkip)
scan_all_files("/path/to/banklogs", checkdeposit)

# check_ip_in_files("12.12.12.12", "/path/to/folder")
# check_deposit_in_files("/path/to/banklogs")



# def CalculateSalary(): # SRP = endast detta
#     return 100

# def CalculateWhatever(): # SRP = endast detta
#     x = 200
#     return x

# def print_decorator( func ):
#     print("Starting")
#     func()
#     print("Ending")

# salary = print_decorator(CalculateSalary)
# whatever = print_decorator(CalculateWhatever)

