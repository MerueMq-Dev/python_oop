from enum import Enum
from abc import ABC

# 1.1
# Выделил в игре Dota 2 несколько базовых классов:
# Класс герой (Hero)
# Объект этого класса — конкретный герой. Например, Slark или Huskar
# потенциальные поля класса Hero
# name - имя героя
# hp - здоровье
# strength, agility, intelligence - характеристики
# move_speed - скорость передвижения
# base_attack - базовый урон
# так же у него могут следующие методы:
# attack() — атаковать другого героя
# move() — передвигаться
# use_ability() — использовать способность

# Класс способности (Ability)
# потенциальные поля класса Ability
# name - название способности
# damage - урон
# cooldown - время перезарядки
# mana_cost - стоимость маны
# так же у него могут следующие методы:
# cast() - применить способность

# Класс предмет (Item)
# потенциальные поля класса Item
# name - название
# bonus_stats - бонусы к характеристикам
# price - стоимость
# так же у него могут следующие методы:
# apply() - применить эффект



# Выделил в телеграмме несколько базовых классов:

# Класс пользователя (User)
# потенциальные поля класса User
# id - уникальный идентификатор пользователя
# username - имя пользователя
# status - статус нахождения в сети (онлайн/офлайн)
# last_active_date - дата последней активности
# так же у него могут следующие методы:
# send_message - отправить сообщение
# change_status - изменить статус

# Класс сообщения (Message)
# потенциальные поля класса Message:
# text — текст сообщения
# sender — отправитель
# timestamp — время отправки
# так же у него могут следующие методы:
# edit() — редактировать сообщение
# delete() — удалить сообщение

# 1.2 Классы
class Attribute(Enum):
    STRENGTH = 1
    AGILITY = 2
    INTELLIGENCE = 3


class Hero(ABC):
    def __init__(
        self,
        name: str,
        hp: float,
        main_attribute: Attribute,
        strength: float,
        agility: float,
        intelligence: float,
        move_speed: int,
        base_attack: int,
    ):
        self.name = name
        self.hp = hp
        self.main_attribute = main_attribute
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.move_speed = move_speed
        self.base_attack = base_attack

    def attack(self, other: "Hero") -> None:
        other.hp -= self.base_attack

    def __str__(self):
        return f"{self.name}: HP={self.hp}, ATK={self.base_attack}"


class Slark(Hero):
    def __init__(self):
        super().__init__(
            name="Slark",
            hp=630,
            main_attribute=Attribute.AGILITY,
            strength=20,
            agility=21,
            intelligence=16,
            move_speed=300,
            base_attack=58,
        )


class Huskar(Hero):
    def __init__(self):
        super().__init__(
            name="Huskar",
            hp=720,
            main_attribute=Attribute.STRENGTH,
            strength=23,
            agility=10,
            intelligence=18,
            move_speed=290,
            base_attack=44,
        )


class HeroManager:
    @staticmethod
    def fight(first: Hero, second: Hero):
        first.attack(second)
        second.attack(first)

# 1.3 Побочный эффект
slark = Slark()
huskar = Huskar()

print("До боя:")
print(slark)
print(huskar)

HeroManager.fight(slark, huskar)

print("После боя:")
print(slark)
print(huskar)