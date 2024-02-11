if __name__ == "__main__":
    class Character:
        """
        Основной класс, описывающий персонажа рпг игры.
        """

        def __init__(self, *, level: int):
            """
            Инициализация персонажа.

            Parameters:
                level (int): Уровень персонажа.
            """
            if not isinstance(level, int):
                raise TypeError("'level' must be of the int type")

            self.level = level
            self.hp = level * self.base_hp

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
                damage (int): Значение урона персонажа.
            """
            damage = self.level * self.base_damage
            return damage

        @property
        def max_hp(self) -> int:
            """
            Максимальное значение здоровья, которое может иметь персонаж.

            Returns:
                max_hitpoints (int): Значение максимального запаса здоровья персонажа.
            """
            max_hp = self.base_hp * self.level
            return max_hp

        def attack(self, *, target: "Character") -> None:
            """
            Функция атаки персонажем другого персонажа(цели).

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
            print(
                f"{self.name} получает {current_damage} урона: текущее значение здоровья {self.name}: {self.hp}")

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

            Returns:
                str: The detailed string representation of the character.
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
        name = "Skeleton"

        @property
        def armor(self) -> int:
            """
            Защита скелета.

            Returns:
                armor (int): Значение защиты скелета.
            """
            armor = super().armor if self.hp_to_percent() >= 50 else super().armor + 2
            return armor


    class Wolf(Character):
        """
        Класс-наследник, описывающий персонажа-волка.
        Способность: увеличение урона на 3, если здоровье волка ниже 30%;
                    если цель - скелет, то постоянное дополнительное увеличение урона на 1.
        """

        name = "Wolf"
        base_hp = 100
        base_damage = 11
        base_armor = 1

        def __init__(self, level: int) -> None:
            """
            Инициализация объекта класса Wolf.

            Parameters:
                level (int): Уровень персонажа-волка.
                additional_damage (int): Дополнительный урон, используется в механике способности волка.
            """
            super().__init__(level=level)
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
            Функция атаки "волком" другого персонажа(цели).
            Учитывает в себе механику способности волка.

            Parameters:
                target (Character): Цель для атаки.
            """
            print(f"{self.name} атакует {target.name}.")
            if type(target) == Skeleton:
                self.additional_damage = 1
            else:
                self.additional_damage = 0
            target.take_damage(damage=self.damage)


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

pass
