# from enum import Enum
# import random
#
#
# class SuperAbility(Enum):
#     CRITICAL_DAMAGE = 1
#     BOOST = 2
#     HEAL = 3
#     SAVE_DAMAGE_AND_REVERT = 4
#
#
# class GameEntity:
#     def __init__(self, name, health, damage):
#         self.__name = name
#         self.__health = health
#         self.__damage = damage
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def health(self):
#         return self.__health
#
#     @health.setter
#     def health(self, value):
#         if value < 0:
#             self.health = 0
#         else:
#             self.__health = value
#
#     @property
#     def damage(self):
#         return self.__damage
#
#     @damage.setter
#     def damage(self, value):
#         self.__damage = value
#
#     def __str__(self):
#         return f'Name: {self.__name}, Health: {self.__health}, Damage: {self.__damage}'
#
#
# class Boss(GameEntity):
#     def __init__(self, name, health, damage):
#         GameEntity.__init__(self, name, health, damage)
#         self.__defence = None
#
#     @property
#     def defence(self):
#         return self.__defence
#
#     def choose_defence(self, heroes):
#         random_hero = random.choice(heroes)
#         self.__defence = random_hero.ability
#
#     def attack(self, heroes):
#         for hero in heroes:
#             if hero.health > 0:
#                 hero.health -= self.damage
#
#     def __str__(self):
#         return f'BOSS ' + super().__str__() + f', defence: {self.__defence}'
#
#
# class Hero(GameEntity):
#     def __init__(self, name, health, damage, ability):
#         GameEntity.__init__(self, name, health, damage)
#         self.__ability = ability
#
#     @property
#     def ability(self):
#         return self.__ability
#
#     def attack(self, boss):
#         if self.health > 0 and boss.health > 0:
#             boss.health -= self.damage
#
#     def apply_super_power(self, boss, heroes):
#         pass
#
#
# class Warrior(Hero):
#     def __init__(self, name, health, damage):
#         Hero.__init__(self, name, health, damage, ability=SuperAbility.CRITICAL_DAMAGE)
#
#     def apply_super_power(self, boss, heroes):
#         if self.health > 0:
#             coefficient = random.randint(2, 5)
#             boss.health -= self.damage * coefficient
#             print(f'Warrior hits critically {self.damage * coefficient}')
#
#
# class Magic(Hero):
#     def __init__(self, name, health, damage):
#         Hero.__init__(self, name, health, damage, ability=SuperAbility.BOOST)
#
#     def apply_super_power(self, boss, heroes):
#         pass
#
#
# class Medic(Hero):
#     def __init__(self, name, health, damage, heal_points):
#         Hero.__init__(self, name, health, damage, ability=SuperAbility.HEAL)
#         self.__heal_points = heal_points
#
#     def apply_super_power(self, boss, heroes):
#         if self.health > 0:
#             for hero in heroes:
#                 if hero.health > 0 and hero != self:
#                     hero.health += self.__heal_points
#
#
# class Berserk(Hero):
#     def __init__(self, name, health, damage):
#         Hero.__init__(self, name, health, damage, ability=SuperAbility.SAVE_DAMAGE_AND_REVERT)
#         self.__blocked_damage = 0
#
#     @property
#     def blocked_damage(self):
#         return self.__blocked_damage
#
#     @blocked_damage.setter
#     def blocked_damage(self, value):
#         self.__blocked_damage = value
#
#     def apply_super_power(self, boss, heroes):
#         pass
#
#
# round_number = 0
#
#
# def print_statistick(boss, heroes):
#     print(f'\n<--- Round {round_number} --->')
#     print(boss)
#     for hero in heroes:
#         print(hero)
#
#
# def is_game_finish(boss, heroes):
#     if boss.health <= 0:
#         print(f'\nHeroes won! {boss.name} is defeat!')
#         return True
#
#     all_heroes_dead = True
#
#     for hero in heroes:
#         if hero.health > 0:
#             all_heroes_dead = False
#             break
#
#     if all_heroes_dead:
#         print('\nBoss won! heroes is defeat!')
#
#     return all_heroes_dead
#
#
# def play_round(boss, heroes):
#     global round_number
#     round_number += 1
#
#     boss.choose_defence(heroes)
#     boss.attack(heroes)
#
#     for hero in heroes:
#         if hero.ability != boss.defence:
#             hero.attack(boss)
#             hero.apply_super_power(boss, heroes)
#
#     print_statistick(boss, heroes)
#
#
# def start_game():
#     boss = Boss(name='Ilidan', health=1000, damage=50)
#     warrior = Warrior(name='Zylong', health=310, damage=20)
#     doc = Medic(name='Inwoker', health=250, damage=15, heal_points=30)
#     magic = Magic(name='Dambldor', health=280, damage=15)
#     berserk = Berserk(name='Gats', health=350, damage=25)
#     assistant = Medic(name='Swan', health=290, damage=5, heal_points=15)
#
#     heroes = [warrior, doc, magic, berserk, assistant]
#
#     print_statistick(boss, heroes)
#
#     while not is_game_finish(boss, heroes):
#         play_round(boss, heroes)
#
#
# start_game()
