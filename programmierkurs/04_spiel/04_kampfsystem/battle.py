import random


class BattleSystem:
    def fight_round(self, player, monster):
        player_hit = random.randint(max(1, player.attack - 3), player.attack + 3)
        monster.take_damage(player_hit)

        if monster.is_alive():
            monster_hit = random.randint(max(1, monster.attack - 2), monster.attack + 2)
            player.take_damage(monster_hit)
            return player_hit, monster_hit
        return player_hit, 0
