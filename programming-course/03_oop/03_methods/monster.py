class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0


gegner = Monster("Slime", 30)
gegner.take_damage(10)
print(gegner.hp)
