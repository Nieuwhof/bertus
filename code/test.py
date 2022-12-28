## testing oop
import random

items = ["Spider","Troll","Vampire","Wolf","Thing", "leech", "Bombardier Bug", "Zombie"]
items2 = [100,80,85,70,65,71,45,90,55,43,23,11,5]

class Monster:
    def __init__(self, name, life):
        self.name = name
        self.life = life
        if name == '':
            self.name = random.choice(items)
            self.life = random.choice(items2)

mon1 = Monster('test',10)
mon2 = Monster('',0) 
mon3 = Monster('',0)  

print(mon1.name, mon1.life)
print(mon2.name, mon2.life)
print(mon3.name, mon3.life)