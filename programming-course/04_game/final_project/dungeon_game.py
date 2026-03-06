import random


class Player:
    def __init__(self, name, hp=100, attack=14):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.potions = 2

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def heal(self):
        if self.potions <= 0:
            print("Keine Heiltränke mehr!")
            return
        self.potions -= 1
        heal_amount = random.randint(12, 22)
        self.hp = min(self.max_hp, self.hp + heal_amount)
        print(f"{self.name} heilt sich um {heal_amount} HP. (HP: {self.hp})")


class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)


class BattleSystem:
    def fight_round(self, player, monster):
        player_damage = random.randint(max(1, player.attack - 4), player.attack + 4)
        monster.take_damage(player_damage)
        print(f"{player.name} trifft {monster.name} für {player_damage} Schaden.")

        if monster.is_alive():
            monster_damage = random.randint(max(1, monster.attack - 3), monster.attack + 3)
            player.take_damage(monster_damage)
            print(f"{monster.name} kontert mit {monster_damage} Schaden.")


class Game:
    MONSTER_POOL = [
        Monster("Slime", 35, 8),
        Monster("Goblin", 45, 10),
        Monster("Skelett", 55, 12),
    ]

    def __init__(self):
        self.player = None
        self.battle = BattleSystem()

    def create_monster(self):
        return random.choice(self.MONSTER_POOL)

    def start(self):
        print("=== Dungeon Quest ===")
        name = input("Wie heißt dein Held? ").strip() or "Held"
        self.player = Player(name)
        print(f"Willkommen, {self.player.name}!\n")

        runde = 1
        while self.player.is_alive() and runde <= 3:
            monster = self.create_monster()
            print(f"\nRunde {runde}: Ein {monster.name} erscheint! ({monster.hp} HP)")

            while monster.is_alive() and self.player.is_alive():
                print(f"\nDeine HP: {self.player.hp} | Tränke: {self.player.potions}")
                print(f"Monster-HP: {monster.hp}")
                action = input("Wähle Aktion [a]ngriff / [h]eilen: ").strip().lower()

                if action == "h":
                    self.player.heal()
                else:
                    self.battle.fight_round(self.player, monster)

            if self.player.is_alive():
                print(f"{monster.name} wurde besiegt!")
                runde += 1

        if self.player.is_alive():
            print("\n🎉 Sieg! Du hast den Dungeon gemeistert.")
        else:
            print("\n💀 Game Over. Versuch es nochmal!")


if __name__ == "__main__":
    Game().start()
