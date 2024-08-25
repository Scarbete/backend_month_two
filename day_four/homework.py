from enum import Enum
import random


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    LIFE_STEAL = 5
    STUN = 6
    SIZE_MANIPULATION = 7


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'Имя: {self.__name}, Здоровье: {self.__health}, Урон: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)
        self.__defence = None
        self.__stunned = False

    @property
    def stunned(self):
        return self.__stunned

    @stunned.setter
    def stunned(self, value):
        if isinstance(value, bool):
            self.__stunned = value
        else:
            raise ValueError('Свойство Stunned должен иметь bool значение')

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        random_hero = random.choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        if self.__stunned:
            print(f'Босс словил стан и пропускает этот раунд!')
            self.__stunned = False
        else:
            for hero in heroes:
                if hero.health > 0:
                    hero.health -= self.damage

    def __str__(self):
        return f'Босс ' + super().__str__() + f', Иммунитет: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        GameEntity.__init__(self, name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0 and boss.health > 0:
            boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, ability=SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            coefficient = random.randint(2, 5)
            boss.health -= self.damage * coefficient
            print(f'Воин наносит критический удар {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, ability=SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            damage_coefficient = random.randint(2, 5)
            for hero in heroes:
                if hero.health > 0 and hero != self:
                    hero.damage += damage_coefficient


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, ability=SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            for hero in heroes:
                if hero.health > 0 and hero != self:
                    hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, ability=SuperAbility.SAVE_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        pass


class Hacker(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.LIFE_STEAL)

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            random_heal_steal_point = random.randint(5, 15)
            random_hero = random.choice(heroes)
            boss.health -= random_heal_steal_point
            if random_hero.health > 0:
                random_hero.health += random_heal_steal_point


class Thor(Hero):
    def __init__(self, name, health, damage):
        """
        __stun_chance - Процентная вероятность оглушения
        """
        Hero.__init__(self, name, health, damage, SuperAbility.STUN)
        self.__stun_chance = 25

    def apply_super_power(self, boss, heroes):
        if self.health > 0:
            stun_randint = random.randint(1, 100)
            if stun_randint <= self.__stun_chance:
                boss.stunned = True
                print(f'{self.name} застанил босса!')


class AntMan(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, SuperAbility.SIZE_MANIPULATION)
        self.__size = 'normal'
        self.__base_damage = damage
        self.__base_health = health

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value in ['normal', 'small', 'large']:
            self.__size = value
        else:
            raise ValueError('Свойство size может иметь значение (normal, large, small)')

    @property
    def base_damage(self):
        return self.__base_damage

    @property
    def base_health(self):
        return self.__base_health

    def apply_super_power(self, boss, heroes):
        """
        Функция супер способности данного героя работает если
        здоровье героя больше 0 и дальше выбирается случайный размер
        это small либо large, и если размер small то увеличивается урон
        иначе если размер будет large то уменьшается урон но
        повышается здоровье
        """
        if self.health > 0:
            new_size = random.choice(['small', 'large'])
            self.__size = new_size

            if self.__size == 'small':
                self.damage = self.__base_damage * 1.5
                print(f'{self.name} уменьшается до маленького размера и наносит больше урона')
            elif self.__size == 'large':
                self.health += 50
                self.damage = self.damage * 0.5
                print(
                    f'{self.name} вырастает до больших размеров, '
                    f'получая дополнительное здоровье, но нанося меньше урона'
                )

    def attack(self, boss):
        """
        Функия атаки героя действует если его и здоровье босса
        больше 0, и если размер героя small либо large то наноситься
        соответствующий урон и дальше размер и урон героя
        становиться нормальным ( дефолтным )
        """
        if self.health > 0 and boss.health > 0:
            if self.__size == 'small' or self.__size == 'large':
                boss.health -= self.damage
            else:
                boss.health -= self.base_damage

            self.__size = 'normal'
            self.damage = self.__base_damage


round_number = 0


def print_statistick(boss, heroes):
    print(f'\n<--- Round {round_number} --->')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finish(boss, heroes):
    if boss.health <= 0:
        print(f'\nHeroes won! {boss.name} is defeat!')
        return True

    all_heroes_dead = True

    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print('\nBoss won! heroes is defeat!')

    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1

    boss.choose_defence(heroes)
    boss.attack(heroes)

    for hero in heroes:
        if hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)

    print_statistick(boss, heroes)


def start_game():
    boss = Boss(name='Ilidan', health=1400, damage=50)
    warrior = Warrior(name='Zylong', health=310, damage=20)
    doc = Medic(name='Inwoker', health=250, damage=15, heal_points=30)
    magic = Magic(name='Dambldor', health=280, damage=15)
    berserk = Berserk(name='Gats', health=350, damage=25)
    assistant = Medic(name='Swan', health=290, damage=5, heal_points=15)
    hacker = Hacker(name='Hacker', health=280, damage=10)
    thor = Thor(name='Thor', health=320, damage=20)
    ant_man = AntMan(name='AntMan', health=270, damage=10)

    heroes = [warrior, doc, magic, berserk, assistant, hacker, thor, ant_man]

    print_statistick(boss, heroes)

    while not is_game_finish(boss, heroes):
        play_round(boss, heroes)


start_game()
