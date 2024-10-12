from random import randint, choice


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
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    def choose_defence(self, heroes_list):
        random_hero = choice(heroes_list)
        self.__defence = random_hero.ability

    def attack(self, heroes_list):
        for hero in heroes_list:
            if hero.health > 0:
                if type(hero) == Berserk and self.__defence != hero.ability:
                    hero.blocked_damage = choice([5, 10])
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    @property
    def defence(self):
        return self.__defence

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes_list):
        coefficient = randint(2, 5)
        boss.health -= coefficient * self.damage
        print(f'Warrior {self.name} hits critically {coefficient * self.damage}.')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')

    def apply_super_power(self, boss, heroes_list):
        attack_increase = randint(1, 10)
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.damage += attack_increase
        print(f'Magic {self.name} increased the attack of all heroes by {attack_increase}.')

class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'REVIVE')
        self.has_revived = False

    def apply_super_power(self, boss, heroes_list):
        if not self.has_revived:
            for hero in heroes_list:
                if hero.health <= 0:
                    hero.health = self.health
                    self.health = 0
                    self.has_revived = True
                    print(f'Witcher {self.name} sacrificed to revive {hero.name}.')
                    break

class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'HACK')
        self.rounds_to_hack = 0

    def apply_super_power(self, boss, heroes_list):
        if self.rounds_to_hack == 0:
            stolen_health = randint(10, 30)
            boss.health -= stolen_health
            random_hero = choice([hero for hero in heroes_list if hero.health > 0])
            random_hero.health += stolen_health
            print(f'Hacker {self.name} stole {stolen_health} health from the boss and gave it to {random_hero.name}.')
            self.rounds_to_hack = 1
        else:
            self.rounds_to_hack -= 1


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health * 2, damage // 2, 'BLOCK')

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                blocked_damage = boss.damage // 5
                hero.health += blocked_damage
                self.health -= blocked_damage
        print(f'Golem {self.name} absorbed part of the damage from other heroes.')

class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STUN')

    def apply_super_power(self, boss, heroes_list):
        if randint(1, 5) == 1:  # 20% шанс оглушения
            print(f'Thor {self.name} stunned the boss!')
            boss.damage = 0

class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_DAMAGE')
        self.__blocked_damage = 0

    def apply_super_power(self, boss, heroes_list):
        boss.health -= self.blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damages to boss.')

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes_list):
        for hero in heroes_list:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


round_number = 0


def is_game_over(boss, heroes_list):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes_list:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def show_statistics(boss, heroes_list):
    print(f' ------------- ROUND {round_number} -------------')
    print(boss)
    for hero in heroes_list:
        print(hero)


def play_round(boss, heroes_list):
    global round_number
    round_number += 1
    boss.choose_defence(heroes_list)
    boss.attack(heroes_list)
    for hero in heroes_list:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes_list)
    show_statistics(boss, heroes_list)


def start_game():
    boss = Boss(name='Minotaur', health=1200, damage=50)

    warrior_1 = Warrior(name='Asterix', health=290, damage=10)
    warrior_2 = Warrior(name='Obelix', health=280, damage=15)
    magic = Magic(name='Alice', health=270, damage=5)
    berserk = Berserk(name='Guts', health=220, damage=10)
    doc = Medic(name='Doc', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Junior', health=300, damage=5, heal_points=5)
    hacker = Hacker(name='Neo', health=200, damage=5)
    witcher = Witcher(name='Gera', health=280, damage=10)
    golem = Golem(name='Rocky', health=400, damage=5)
    thor = Thor(name='Thor', health=300, damage=15)


    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant, witcher, golem, hacker, thor]
    show_statistics(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()