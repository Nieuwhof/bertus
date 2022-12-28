## testing oop
import random

items = ["Spider","Troll","Vampire","Wolf","Thing", "leech", "Bombardier Bug", "Zombie"]
items2 = [100,80,85,70,65,71,45,90,55,43,23,11,5]

class player:
    def __init__(self):
        life = 100
        name = 'Player'
        self.name = name
        self.life = life
    
    def GetLife(self):
        return self.life

    def SetLife(self,num):
        self.life = num

class Monster:
    def __init__(self):
        name = random.choice(items)
        life = random.choice(items2)
        self.name = name
        self.life = life

mon1 = Monster()
play = player()
  

print(mon1.name, mon1.life)
print(play.name, play.life)

play.SetLife(30)
print(play.GetLife())

