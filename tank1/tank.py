import random


class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive=True
        self.ammo=5
        self.armor=60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def fire_at(self, enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")


meuTanque1 = Tank("Bob")
meuTanque2 = Tank("Jack")
meuTanque3 = Tank("Igor")
meuTanque4 = Tank("Gui")
meuTanque5 = Tank("Tony")

arraytank = [meuTanque1, meuTanque2, meuTanque3, meuTanque4,meuTanque5]
randomtank1 = random.randint(0, len(arraytank) - 1)
randomtank2 = randomtank1

while randomtank1 == randomtank2:
    randomtank2 = random.randint(0, len(arraytank) -1)

print(len(arraytank))
print(randomtank1)
print(randomtank2)

arraytank[randomtank1].fire_at(arraytank[randomtank2])

print(arraytank[randomtank1])
print(arraytank[randomtank2])