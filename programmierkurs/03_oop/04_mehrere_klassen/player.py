class Player:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power

    def attack(self, monster):
        monster.take_damage(self.attack_power)
