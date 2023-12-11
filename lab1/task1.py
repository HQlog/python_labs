import doctest


class Number:
    def __init__(self, value: float, sign: str):

        """
        Cоздание и подготовка к работе объекта "Число"

        :param value: Значение числа
        :param sign: Знак числа

        Примеры:
        >>> num = Number(5,"+") # инициализация экземпляра класса
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Число должно быть int или float")
        self.attr1 = value

        if sign is not ("+" or "-"):
            raise ValueError("Знак числа должен быть + или - и передан в формате str")
        self.attr2 = sign

    def is_num_pos(self) -> bool:
        """
        Функция которая проверяет положительное ли число

        :return: Положительное ли число

        Примеры:
        >>> num = Number(5,"+")
        >>> num.is_num_pos()
        """
        ...

    def is_even(self) -> bool:
        """
        Функция которая проверяет четное ли число

        :return: Четное ли число

        Примеры:
        >>> num = Number(5,"+")
        >>> num.is_even()
        """
        ...

    def change_value(self, new_value):
        """
        Функция изменяющая значение числа

        :param new_value: Новое значение числа
        :raise TypeError: Если тип переданного нового значения не корректен (не int или float), то возвращается ошибка

        :return: число с измененным значением

        Примеры:
        >>> num = Number(5,"+")
        >>> num.change_value(6)
        """
        ...


class Lamp:
    def __init__(self, brightness: float, status: bool):

        """
        Cоздание и подготовка к работе объекта "Лампа"

        :param brightness: Числовое значение яркости лампы от 0 до 10
        :param status: статус лампы где True включена False выключена

        Примеры:
        >>> lamp = Lamp(5, True) # инициализация экземпляра класса
        """
        if not isinstance(brightness, (int, float)):
            raise TypeError("Яркость должна быть int или float")
        if not 0 <= brightness <= 10:
            raise ValueError("Яркость должна находится в передлах от 0 до 10")
        self.attr1 = brightness

        if not isinstance(status, bool):
            raise ValueError("Состояние должно быть True или False")
        self.attr2 = status

    def change_lamp_status(self) -> None:
        """
        Функция которая меняет статус лампы на противоположный

        :return: Измененная лампа

        Примеры:
        >>> lamp = Lamp(5, False)
        >>> lamp.change_lamp_status()
        """
        ...

    def is_on(self) -> bool:
        """
        Функция которая проверяет включена ли лампа

        :return: включена ли лампа

        Примеры:
        >>> lamp = Lamp(5,True)
        >>> lamp.is_on()
        """
        ...

    def change_brightness(self, new_brightness):
        """
        Функция изменяющая значение яркости лампы

        :param new_brightness: Новое значение яркости

        :raise TypeError: Если тип переданного нового значения не корректен (не int или float), то возвращается ошибка
        :raise ValueError: Если переданное значение не лежит в пределах от 0 до 10, то возвращается ошибка

        :return: Лампа с измененным значением яркости

        Примеры:
        >>> lamp = Lamp(5, True)
        >>> lamp.change_brightness(6)
        """
        ...


class Sword:
    def __init__(self, sharpness: int, length: float):

        """
        Cоздание и подготовка к работе объекта "Меч"

        :param sharpness: Числовое значение заточки меча от 0 до 100
        :param length: длинна меча

        Примеры:
        >>> sword = Sword(81, 10) # инициализация экземпляра класса
        """
        if not isinstance(sharpness, int):
            raise TypeError("Острота меча должна быть типа int")
        self.attr1 = sharpness

        if not isinstance(length, (int, float)):
            raise TypeError("Длинна меча должна быть типа float")
        if length < 0:
            raise ValueError("Длинна меча не может быть меньше нуля")
        self.attr2 = length

    def change_sharpness(self, new_sharpness) -> None:
        """
        Функция которая изменяет остроту меча

        :param new_sharpness: Новое значение остроты

        :raise TypeError: Если тип переданного нового значения не корректен (не int), то возвращается ошибка
        :raise ValueError: Если переданное значение не лежит в пределах от 0 до 100, то возвращается ошибка

        :return: Мечь с измененной остротой

        Примеры:
        >>> sword = Sword(65, 10)
        >>> sword.change_sharpness(100)
        """
        ...

    def change_length(self, new_length) -> None:
        """
        Функция которая изменяет длинну меча

        :param new_length: Новое значение длинны

        :raise TypeError: Если тип переданного нового значения не корректен (не int), то возвращается ошибка
        :raise ValueError: Если переданное значение меньше 0, то возвращается ошибка

        :return: меч с измененной длинной

        Примеры:
        >>> sword = Sword(30, 10)
        >>> sword.change_length(50)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
