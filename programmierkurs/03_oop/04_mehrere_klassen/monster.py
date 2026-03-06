class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
