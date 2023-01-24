import random

class Human:
    def __init__(self, name):
        self.name = name

class Player(Human):
    Counter = 0
    def __init__(self, name):
        super().__init__(name)
        Player.Counter += 1
        self.index = Player.Counter
        self.team = ''

    def set_team(self,team):
        self.team = team

    def get_team(self):
        return self.team

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name + ' ' + self.team

listName = ["Hossein", "Maziyar", "Akbar", "Nima", "Mehdi", "Farhad", "Mohammad", "Khashayar", "Milad", "Mostafa",
                  "Amin", "Saeed", "Pouya", "Pourya", "Reza", "Ali", "Behzad",
                  "soheil", "Behrouz", "Shahrouz", "Saman", "Mohsen"]

myplayer = []
for i in range(0,22):
    index = random.randint(0, len(listName) - 1)
    myplayer.append(Player(listName[index]))
    listName.pop(index)
    
numList = []
for i in range(0,22):
    numList.append(i)

for i in range(0, 11):
    index = random.randint(0, len(numList)-1)
    myplayer[numList[index]].set_team('A')
    numList.pop(index)
    index = random.randint(0, len(numList)-1)
    myplayer[numList[index]].set_team('B')
    numList.pop(index)

for i in range(0,22):
    print(myplayer[i])
