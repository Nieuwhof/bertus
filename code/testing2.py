## This is to test OOP python

class character:
    def __init__(self, name, inventorybag, life, weapon):
        self.name = name
        self.inventorybag = inventorybag
        self.life = int(life)
        self.weapon = weapon

class room:
    def __init__(self, roomname, door, window, monster, goldcoins, lifedamage, weapon ):
        self.roomname = roomname
        self.door = door
        self.window = window
        self.monster = monster
        self.goldcoins = float(goldcoins)
        self.lifedamage = int(lifedamage)
        self.weapon = weapon

character1 = character("Bertus", "empty", 100, "nothing")
theroom = room("porch", "north", "none", "none", "1", 0, "none")

print(character1.name," is standing outside a house with a bad full off",character1.inventorybag)
character1.inventorybag = "stuff"
print(character1.name," is standing outside a house with a bad full off",character1.inventorybag)