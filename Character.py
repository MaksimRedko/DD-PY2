class Character:
    """
    Основной класс, описывающий персонажа рпг игры.
    """

    def __init__(self, name: str, level: int, base_hp: int, base_damage: int, base_armor: int):
        """
        Инициализация персонажа.
        Parameters:
            name (str): Имя персонажа.
            level (int): Уровень персонажа.
            base_hp (int): Базовое здоровье персонажа.
            base_damage (int): Базовый урон персонажа.
            base_armor (int): Базовая броня персонажа.
        """
        if not isinstance(name, str):
            raise TypeError("'name' must be of the str type")

        if not isinstance(level, int):
            raise TypeError("'level' must be of the int type")
        if level <= 0:
            raise ValueError("level must be positive")

        if not isinstance(base_hp, int):
            raise TypeError("'base_hp' must be of the int type")
        if base_hp <= 0:
            raise ValueError("base_hp must be positive")

        if not isinstance(base_damage, int):
            raise TypeError("'base_damage' must be of the int type")
        if base_damage <= 0:
            raise ValueError("base_damage must be positive")

        if not isinstance(base_armor, int):
            raise TypeError("'base_armor' must be of the int type")
        if base_armor < 0:
            raise ValueError("base_armor must be positive")

        self.name = name
        self.level = level
        self.base_hp = base_hp
        self.base_damage = base_damage
        self.base_armor = base_armor
        self.hp = self.level * self.base_hp

    @property
    def armor(self) -> int:
        """
        Защита персонажа.
        Returns:
            armor (int): Значение защиты персонажа.
        """
        armor = self.base_armor
        return armor

    @property
    def damage(self) -> int:
        """
        Урон персонажа.
        Returns:
            damage (int): Значение наносимого урона.
        """
        damage = self.level * self.base_damage
        return damage

    @property
    def max_hp(self) -> int:
        """
        Максимальное значение здоровья, которое может иметь персонаж.
        Returns:
            max_hp (int): Значение максимального запаса здоровья персонажа.
        """
        max_hp = self.base_hp * self.level
        return max_hp

    def attack(self, *, target: "Character") -> None:
        """
        Метод атаки персонажа другого персонажа(цели).
        Parameters:
            target (Character): Цель, которую атакует персонаж.
        """
        print(f"{self.name} атакует {target.name}.")
        target.take_damage(damage=self.damage)

    def take_damage(self, *, damage: int) -> None:
        """
        Функция получения урона персонажем.
        Parameters:
            damage (int): Значение получаемого урона.
        """
        current_damage = damage - self.armor if self.armor <= damage else 0
        self.hp -= damage - self.armor if self.armor <= damage else 0
        if self.hp <= 0:
            self.hp = 0
        print(f"{self.name} получает {current_damage} урона. Текущее значение здоровья {self.name}: {self.hp}")

    def is_alive(self) -> bool:
        """
        Функция, проверяющая жив персонаж или нет.
        Returns:
            bool: True если персонаж жив, False в противном случае.
        """
        return self.hp > 0

    def hp_to_percent(self) -> int:
        """
        Функция, возвращающая текущее значение запаса здоровья в процентном виде от максимального(изначального).
        Используется в механике способностей.
        Returns:
            hp_percents (int): Значение текущего здоровья в процентах.
        """
        hp_percents = self.hp * 100 / self.max_hp
        return round(hp_percents)

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта класса Character, удобное для пользователя.
        """
        return '{:^10s}({:d} lvl) - Health: {:^10d} | Damage: {:^10d} | Armor: {:^10d}'.format(self.name,
                                                                                               self.level,
                                                                                               self.hp,
                                                                                               self.damage,
                                                                                               self.armor)

    def __repr__(self) -> str:
        """
        Возвращает строку-информацию об объекте класса Character.
        """
        return f"name: '{self.name}', level: {self.level}, hp: {self.hp}, damage: {self.damage}, armor: {self.armor}"


class Skeleton(Character):
    """
    Класс-наследник, описывающий персонажа-скелета.
    Способность: увеличение защиты на 2 если здоровье скелета ниже 50%.
    """

    base_hp = 80
    base_damage = 11
    base_armor = 2

    def __init__(self, level: int):
        """
        Инициализация объекта класса Skeleton.
        Parameters:
            level (int): Уровень персонажа-скелета.
        """
        super().__init__(name="Skeleton", level=level, base_hp=Skeleton.base_hp,
                         base_damage=Skeleton.base_damage, base_armor=Skeleton.base_armor)

    @property
    def armor(self) -> int:
        """
        Защита скелета.
        Returns:
            armor (int): Значение защиты скелета.
        """
        armor = super().armor if self.hp_to_percent() >= 50 else super().armor + 2
        return armor

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self):
        return f'name: \'{self.name}\', level: {self.level}, hp: {self.hp}, damage: {self.damage}, armor: {self.armor}, ' \
               f'ability: Increase defense by 2 if the skeleton\'s health is below 50%.'


class Wolf(Character):
    """
    Класс-наследник, описывающий персонажа-волка.
    Способность: увеличение урона на 3, если здоровье волка ниже 30%;
                    если цель - скелет, то постоянное дополнительное увеличение урона на 1.
    """

    base_hp = 100
    base_damage = 11
    base_armor = 1

    def __init__(self, level: int):
        """
        Инициализация объекта класса Wolf.
        Parameters:
            level (int): Уровень персонажа-волка.
            additional_damage (int): Дополнительный урон, используется в механике способности волка.
        """
        super().__init__(name="Wolf", level=level, base_hp=Wolf.base_hp, base_damage=Wolf.base_damage,
                         base_armor=Wolf.base_armor)
        self.additional_damage = 0

    @property
    def damage(self) -> int:
        """
            Урон персонажа-волка.
        Returns:
            damage (int): Значение наносимого урона.
        """
        damage = super().damage + 3 if self.hp_to_percent() < 30 else super().damage
        return damage + self.additional_damage

    def attack(self, *, target: "Character") -> None:
        """
        Перегруженный метод атаки "волком" другого персонажа(цели).
        Учитывает в себе механику способности волка.
        Parameters:
            target (Character): Цель для атаки.
        """
        print(f"{self.name} атакует {target.name}.")
        if type(target) == Skeleton:
            self.additional_damage = 1
        else:
            self.additional_damage = 0
        super().attack(target=target)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"name: '{self.name}', level: {self.level}, hp: {self.hp}, damage: {self.damage}, armor: {self.armor}, " \
               f"ability: Ability: Increase damage by 3 if the wolf's health is below 30%; if the target is a " \
               f"skeleton, permanent additional damage increase by 1."


def fight(character1: "Character", character2: "Character") -> None:
    """
    Функция, симулирующая бой между двумя персонажами.
    Parameters:
        character1 (Character): Первый персонаж.
        character2 (Character): Второй персонаж.
    """
    print('{:^40s}'.format("-----Fight is start-----"))
    while character1.is_alive() and character2.is_alive():  # пока оба персонажа живы, бой продолжается.
        character1.attack(target=character2)
        # если после первого хода оба персонажа по-прежнему живы, бой продолжается.
        if character1.is_alive() and character2.is_alive():
            print('{:^40s}'.format("------------------------"))
            character2.attack(target=character1)
            print('{:^40s}'.format("------------------------"))
            print(character1)
            print(character2)
            print('{:^40s}'.format("------------------------"))
    winners = character1.name if character1.is_alive() else character2.name  # определение победителя в бою
    print(f"Winners: {winners}")


# создание двух персонажей первого уровня
skeleton = Skeleton(level=1)
wolf = Wolf(level=1)

print(skeleton)  # Skeleton (1 lvl) - Health:     80     | Damage:     11     | Armor:     2
print(wolf)  # Wolf   (1 lvl) - Health:    100     | Damage:     11     | Armor:     1

fight(skeleton, wolf)

print(skeleton)  # Skeleton (1 lvl) - Health:     0      | Damage:     11     | Armor:     4
print(wolf)  # Wolf   (1 lvl) - Health:     10     | Damage:     15     | Armor:     1
