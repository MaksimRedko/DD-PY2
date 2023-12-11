import doctest
from math import sqrt
from typing import Union


class Robot:
    def __init__(self, model: str, battery_level: int):
        """
        Класс, описывающий робота.

        :param model: Модель робота.
        :type model: str
        :param battery_level: Уровень заряда батареи робота.
        :type battery_level: Union[int, float]

        Примеры:
        >>> robot_killer = Robot("Killer 3000", 100)
        >>> robot_helper = Robot("HeLp - 2023", 50)
        """

        if not isinstance(model, str):
            raise TypeError("Аргумент model должен быть типа String")
        self.model = model

        if not isinstance(battery_level, int):
            raise TypeError("Аргумент battery_level должен быть типа Integer")

        if battery_level < 0 or battery_level > 100:
            raise ValueError("Уровень заряда батареи должен быть в диапазоне от 0 до 100")
        self.battery_level = battery_level

    def move(self, distance: Union[int, float]):
        """
        Метод описывает движение робота на заданное расстояние в метрах.

        Если расстояние положительно - робот движется вперед.
        Если расстояние отрицательно - робот движется назад.
        Если расстояние равно 0 - робот стоит на месте.

        :param distance: Расстояние для движения.
        :type distance: Union[int, float]

        Примеры:

        >>> robot_helper = Robot("HeLp - 2023", 50)
        >>> robot_helper.move(-3)
        Робот HeLp - 2023 сдвинулся назад на 3 м.

        >>> robot_helper.move(0)
        Робот HeLp - 2023 никуда не сдвинулся

        >>> robot_killer = Robot("Killer 3000", 100)
        >>> robot_killer.move(3000)
        Робот Killer 3000 сдвинулся вперед на 3000 м.
        """
        if distance > 0:
            print(f"Робот {self.model} сдвинулся вперед на {distance} м.")

        if distance < 0:
            print(f"Робот {self.model} сдвинулся назад на {abs(distance)} м.")

        if distance == 0:
            print(f"Робот {self.model} никуда не сдвинулся")

    def charge(self):
        """
        Метод описывает процесс зарядки батареи робота.

        Один вызов метода заряжает робота на 25%

        Примеры:
        >>> robot_helper = Robot("HeLp - 2023", 50)
        >>> robot_helper.charge()
        Робот HeLp - 2023 зарядился с 50 до 75

        >>> robot_killer = Robot("Killer 3000", 100)
        >>> robot_killer.charge()
        Робот Killer 3000 не нуждается в зарядке

        """
        old_battery_level = self.battery_level
        if old_battery_level == 100:
            print(f"Робот {self.model} не нуждается в зарядке")
            return

        elif self.battery_level + 25 > 100:
            self.battery_level = 100
        else:
            self.battery_level += 25
        print(f"Робот {self.model} зарядился с {old_battery_level} до {self.battery_level}")
        return


class Point:
    """
    Класс описывающий точку, заданную на двумерной плоскости.

    :param coord_x: Координата точки по оси X.
    :type coord_x: Union[int, float]
    :param coord_y: Координата точки по оси Y.
    :type coord_y: Union[int, float]

    Примеры:
    >>> point_one = Point(-1,20)
    >>> point_two = Point(10,-1)

    """

    def __init__(self, coord_x: Union[int, float], coord_y: Union[int, float]):

        if not isinstance(coord_x, (int, float)):
            raise TypeError("Координата точки по оси Х должна быть либо Integer, либо Float")
        self.coord_x = coord_x

        if not isinstance(coord_y, (int, float)):
            raise TypeError("Координата точки по оси Y должна быть либо Integer, либо Float")
        self.coord_y = coord_y

    def define_a_quarter(self):
        """
        Метод определяет в какой из четвертей находится точка.

        Примеры:
        >>> point_one = Point(-1,20)
        >>> point_one.define_a_quarter()
        Точка находится во второй четверти

        >>> point_two = Point(10,-1)
        >>> point_two.define_a_quarter()
        Точка находится в четвертой четверти

        """
        temp_parametr = self.coord_x * self.coord_y
        if temp_parametr == 0:
            print("Точка находится на границе четвертей")
            return
        if temp_parametr > 0:
            if self.coord_x > 0:
                print("Точка находится в первой четверти")
                return
            else:
                print("Точка находится в третьей четверти")
                return

        if temp_parametr < 0:
            if self.coord_x > 0:
                print("Точка находится в четвертой четверти")
                return
            else:
                print("Точка находится во второй четверти")
                return

    def distance_from_origin(self):
        """
        Метод определяет расстояние меджду заданной точкой и центром координатной плоскости(точка с координатами (0,0))

        Примеры:
        >>> point_one = Point(0,20)
        >>> point_one.distance_from_origin()
        Точка находится на расстоянии 20.0 от центра

        >>> point_two = Point(3,-4)
        >>> point_two.distance_from_origin()
        Точка находится на расстоянии 5.0 от центра
        """
        res = sqrt(self.coord_x ** 2 + (self.coord_y) ** 2)

        print(f"Точка находится на расстоянии {res} от центра")


class Student:
    """
    Класс описывает студента.

    :param name: Имя Студента.
    :type name: str
    :param institute: Институт, на котором обучается студент.
    :type institute: str
    :param average_mark: Средняя оценка студента по всем предметам (от 0 до 5 включительно)
    :type average_mark: Union[int, float]

    Примеры:
    >>> student_boy = Student("Олег", "ИКНК", 3.33)
    >>> student_girl = Student("Наталья", "ГИ", 5)
    """

    def __init__(self, name: str, institute: str, average_mark: Union[int, float]):
        if not isinstance(name, str):
            raise TypeError("Аргумент 'name' должен быть типа String ")
        self.name = name

        if not isinstance(institute, str):
            raise TypeError("Аргумент 'institute' должен быть типа String ")
        self.institute = institute

        if not isinstance(average_mark, (int, float)):
            raise TypeError("Аргумент 'average_mark' должен быть типа int,либо типа float ")

        if average_mark < 0 or average_mark > 5:
            raise ValueError("Значение аргумента 'average_mark' должно быть от 0 до 5 влючительно")
        self.average_mark = average_mark

    def evaluate_performance(self):
        """
        Метод определяет насколько хорошо учится студент и соотносит его с одной из категорий:
        средняя оценка = 5 - отличник
        средняя оценка между 4 и 5 - хорошист
        средняя оценка между 3 и 4 - троечник
        средняя оценка ниже 3 - неудовлетворительно

        Примеры:
    >>> student_boy = Student("Олег", "ИКНК", 3.33)
    >>> student_boy.evaluate_performance()
    Студент является троечником

    >>> student_girl = Student("Наталья", "ГИ", 5.0)
    >>> student_girl.evaluate_performance()
    Студент является отличником

        """
        if self.average_mark == 5:
            print("Студент является отличником")
            return

        if 5 > self.average_mark >= 4:
            print("Студент является хорошистом")
            return

        if 4 > self.average_mark >= 3:
            print("Студент является троечником")
            return

        if self.average_mark < 3:
            print("Студент учится неудовлетворительно")
            return

    def change_institute(self, new_institute: str):
        """
        Метод позволяет студенту перевестись в желаемый иститут.

        Если средняя оценка студент является хорошистом или отличником, то он сможет перевестись, в противном случае не сможет.

        Примеры:
    >>> student_boy = Student("Олег", "ИКНК", 3.33)
    >>> student_boy.change_institute("ГИ")
    Студенто было отказано в переводе из института ИКНК в институт ГИ

    >>> student_girl = Student("Наталья", "ГИ", 5)
    >>> student_girl.change_institute("ИКНК")
    Студент успeшно переверлся из института ГИ в институт ИКНК
        """
        if self.average_mark >= 4:
            print(f"Студент успeшно переверлся из института {self.institute} в институт {new_institute}")
            self.institute = new_institute
            return
        else:
            print(f"Студенто было отказано в переводе из института {self.institute} в институт {new_institute}")
            return


if __name__ == "__main__":
    doctest.testmod()
    pass
