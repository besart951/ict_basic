from player import Player
from monster import Monster

spieler = Player("Nora", 12)
monster = Monster("Goblin", 35)

while monster.hp > 0:
    spieler.attack(monster)
    print(f"{monster.name} hat noch {monster.hp} HP")

print("Kampf beendet!")
