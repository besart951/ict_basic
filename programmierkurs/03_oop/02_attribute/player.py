class Player:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


spieler = Player("Aria", 100, 1)
print(spieler.name, spieler.hp, spieler.level)
