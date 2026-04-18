from abc import ABC, abstractmethod
import random

# Базовый класс для предметов

class Item(ABC):
    def __init__(self, name, price, is_passive):
        self._name = name
        self._price = price
        self._is_passive = is_passive

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

    @abstractmethod
    def apply_passive(self, hero):
        pass

    def use(self, hero):
        if self._is_passive:
            print(f"{self._name} — пассивный предмет")
        else:
            self._use_impl(hero)

    @abstractmethod
    def _use_impl(self, hero):
        pass


# Предметы

class PowerTreads(Item):
    def __init__(self):
        super().__init__("Power Treads", 1400, False)

    def apply_passive(self, hero):
        hero._increase_stat("agility", 10)

    def _use_impl(self, hero):
        print(f"{hero.get_name()} переключает атрибут")


class BlinkDagger(Item):
    def __init__(self):
        super().__init__("Blink Dagger", 2250, False)

    def apply_passive(self, hero):
        pass

    def _use_impl(self, hero):
        print(f"{hero.get_name()} блинкуется!")


class HeartOfTarrasque(Item):
    def __init__(self):
        super().__init__("Heart of Tarrasque", 5000, True)

    def apply_passive(self, hero):
        hero._increase_hp(250)

    def _use_impl(self, hero):
        pass


# Базовый класс для героев

class Hero:
    MAX_SLOTS = 6

    def __init__(self, name, hp, strength, agility, intelligence, gold):
        self.__name = name
        self.__hp = hp
        self.__strength = strength
        self.__agility = agility
        self.__intelligence = intelligence
        self.__gold = gold

        self.__items = []

    def buy_item(self, item: Item):
        if len(self.__items) >= Hero.MAX_SLOTS:
            print("Нет свободных слотов")
            return

        if self.__gold < item.get_price():
            print("Недостаточно золота")
            return

        self.__gold -= item.get_price()
        self.__items.append(item)
        item.apply_passive(self)

        print(f"{self.__name} купил {item.get_name()}")

    def sell_item(self, index):
        if 0 <= index < len(self.__items):
            item = self.__items.pop(index)
            refund = item.get_price() // 2
            self.__gold += refund

            print(f"{self.__name} продал {item.get_name()} за {refund}")

    def use_item(self, index):
        if 0 <= index < len(self.__items):
            self.__items[index].use(self)

    def show_items(self):
        if not self.__items:
            print("Инвентарь пуст")
            return

        for i, item in enumerate(self.__items):
            print(f"{i}: {item.get_name()}")

    def _increase_stat(self, stat, value):
        if stat == "strength":
            self.__strength += value
        elif stat == "agility":
            self.__agility += value
        elif stat == "intelligence":
            self.__intelligence += value

    def _increase_hp(self, value):
        self.__hp += value

    def get_name(self):
        return self.__name

    def get_gold(self):
        return self.__gold

    def __str__(self):
        return (f"{self.__name}: HP={self.__hp}, "
                f"STR={self.__strength}, AGI={self.__agility}, "
                f"INT={self.__intelligence}, Gold={self.__gold}")


# Магазин

class Shop:
    def __init__(self):
        self.__items = [
            PowerTreads(),
            BlinkDagger(),
            HeartOfTarrasque()
        ]

    def show_items(self):
        print("Магазин:")
        for i, item in enumerate(self.__items):
            print(f"{i}: {item.get_name()} ({item.get_price()})")

    def buy(self, hero: Hero, index):
        if 0 <= index < len(self.__items):
            item = self.__items[index]
            hero.buy_item(item)


# Демо

hero = Hero("Slark", 600, 20, 25, 15, 4000)
shop = Shop()

print(hero)
shop.show_items()

print()
shop.buy(hero, 0)  # Power Treads
shop.buy(hero, 1)  # Blink
shop.buy(hero, 2)  # не хватит
print(hero)
hero.show_items()
hero.use_item(1)
hero.sell_item(0)

print()
print("Финал:")
print(hero)

# 4.2
# Полиморфизм — это когда один и тот же код может работать с разными типами объектов, а нужное
# поведение выбирается автоматически в зависимости от того, какой объект передали.
# В примере с Animal, Cat и Bird в основном показан полиморфизм подтипов: есть общий базовый
# класс, и у наследников по-разному реализован метод foo. Поэтому при вызове animal.foo
# будет выполняться разная логика для кота и птицы.
# А вот параметрический полиморфизм тут выражен слабо, потому что функция всё-таки завязана
# на тип Animal. В чистом виде в Python он скорее выглядит как “мне не важно, что это за
# объект — главное, чтобы у него был нужный метод”.


class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def fill_animals_list(animals: list[Animal]):
    animals.clear()
    for _ in range(500):
        if random.random() < 0.5:
            animals.append(Bird())
        else:
            animals.append(Cat())

animals:list[Animal] = []

fill_animals_list(animals)

for animal in animals:
    animal.foo()

# Вывод получился таким, потому что каждый объект на самом деле каждый объект “помнит”, кто
# он есть (Cat или Bird), поэтому вызывается его собственная версия метода foo() и от типа
# переменной это никак не зависит.