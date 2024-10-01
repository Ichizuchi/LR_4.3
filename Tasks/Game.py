import random

class Soldier:
    _id_counter = 1  
    
    def __init__(self, team):
        self.id = Soldier._id_counter
        Soldier._id_counter += 1
        self.team = team
    
    def follow_hero(self, hero):
        print(f"Солдат {self.id} следует за героем {hero.id} команды {hero.team}")

class Hero:
    _id_counter = 1  
    
    def __init__(self, team):
        self.id = Hero._id_counter
        Hero._id_counter += 1
        self.team = team
        self.level = 1
    
    def level_up(self):
        self.level += 1
        print(f"Герой {self.id} команды {self.team} повысил уровень до {self.level}")

hero_team_1 = Hero(team=1)
hero_team_2 = Hero(team=2)

soldiers_team_1 = []
soldiers_team_2 = []

for _ in range(10):
    team = random.choice([1, 2])
    soldier = Soldier(team=team)
    
    if team == 1:
        soldiers_team_1.append(soldier)
    else:
        soldiers_team_2.append(soldier)

print(f"Солдаты команды 1: {len(soldiers_team_1)}")
print(f"Солдаты команды 2: {len(soldiers_team_2)}")

if len(soldiers_team_1) > len(soldiers_team_2):
    hero_team_1.level_up()
elif len(soldiers_team_2) > len(soldiers_team_1):
    hero_team_2.level_up()
else:
    print("Обе команды имеют одинаковое количество солдат")

if soldiers_team_1:
    soldiers_team_1[0].follow_hero(hero_team_1)
