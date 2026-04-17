from enum import Enum
from abc import ABC


class Attribute(Enum):
    STRENGTH = 1
    AGILITY = 2
    INTELLIGENCE = 3


class Hero(ABC):
    def __init__(self, name, hp, main_attribute, strength, agility, intelligence):
        self.__name = name
        self.__hp = hp
        self.__main_attribute = main_attribute
        self.__strength = strength
        self.__agility = agility
        self.__intelligence = intelligence

    # --- методы (работа с состоянием) ---
    def is_alive(self):
        return self.__hp > 0

    def attack(self, other):
        damage = self.__calculate_damage()
        other.__take_damage(damage)

    def heal(self, amount):
        if amount > 0:
            self.__hp += amount

    def get_hp(self):
        return self.__hp

    def get_name(self):
        return self.__name

    # --- приватные методы ---
    def __calculate_damage(self):
        if self.__main_attribute == Attribute.STRENGTH:
            return self.__strength
        elif self.__main_attribute == Attribute.AGILITY:
            return self.__agility
        else:
            return self.__intelligence

    def __take_damage(self, damage):
        self.__hp -= damage

    def __str__(self):
        return f"{self.__name}: HP={self.__hp}"


class Slark(Hero):
    def __init__(self):
        super().__init__("Slark", 630, Attribute.AGILITY, 20, 21, 16)

    # уникальные методы
    def steal_agility(self):
        print("Slark ворует ловкость")

    def shadow_dance(self):
        print("Slark уходит в невидимость")


class Huskar(Hero):
    def __init__(self):
        super().__init__("Huskar", 720, Attribute.STRENGTH, 23, 10, 18)

    # уникальные методы
    def berserk(self):
        print("Huskar входит в берсерк")

    def burning_spear(self):
        print("Huskar кидает горящее копьё")



# 5.2
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    # --- базовые операции ---
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    def _withdraw(self, amount):
        self.__balance -= amount

    def get_owner(self):
        return self.__owner


class DebitAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.get_balance():
            self._withdraw(amount)
        else:
            print("Недостаточно средств")

    def pay(self, amount):
        print("Оплата дебетовой картой")
        self.withdraw(amount)


class CreditAccount(BankAccount):
    def __init__(self, owner, balance, limit):
        super().__init__(owner, balance)
        self.__limit = limit

    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.__limit:
            self._withdraw(amount)
        else:
            print("Превышен кредитный лимит")

    def pay(self, amount):
        print("Оплата кредитной картой")
        self.withdraw(amount)



class Payment:
    def __init__(self, amount):
        self._amount = amount

    def execute(self, account: BankAccount):
        pass


class OnlinePayment(Payment):
    def execute(self, account: BankAccount):
        print("Онлайн-платёж")
        account._withdraw(self._amount)

    def confirm(self):
        print("Подтверждение по SMS")


class TerminalPayment(Payment):
    def execute(self, account: BankAccount):
        print("Платёж через терминал")
        account._withdraw(self._amount)

    def print_receipt(self):
        print("Печать чека")
