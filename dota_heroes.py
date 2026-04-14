from enum import Enum
from abc import ABC


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

    # ---- МЕТОДЫ (поведение) ----

    def calculate_damage(self) -> float:
        if self.main_attribute == Attribute.STRENGTH:
            return self.base_attack + self.strength
        elif self.main_attribute == Attribute.AGILITY:
            return self.base_attack + self.agility
        else:
            return self.base_attack + self.intelligence

    def attack(self, other: "Hero") -> None:
        damage = self.calculate_damage()
        other.take_damage(damage)

    def take_damage(self, damage: float):
        self.hp -= damage

    def heal(self, amount: float):
        self.hp += amount

    def is_alive(self) -> bool:
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: HP={self.hp}"


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

    # уникальный метод
    def steal_agility(self, other: Hero):
        self.agility += 1
        other.agility -= 1


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

    # уникальный метод
    def berserk(self):
        self.base_attack += 10
        self.hp -= 20


class HeroManager:
    @staticmethod
    def fight(first: Hero, second: Hero):
        if first.is_alive():
            first.attack(second)
        if second.is_alive():
            second.attack(first)


slark = Slark()
huskar = Huskar()

print("До боя:")
print(slark)
print(huskar)

slark.steal_agility(huskar)
huskar.berserk()

HeroManager.fight(slark, huskar)

print("После боя:")
print(slark)
print(huskar)