class Device:
    """Базовый класс Устройство."""

    def __init__(self, brand: str, model: str, year_of_release: int):
        """
        Конструктор класса Устройство.

        Args:
            brand (str): Бренд устройства.
            model (str): Модель устройства.
            year_of_release (int): Год выпуска устройства.
        """
        self._brand = brand  # Используем инкапсуляцию для скрытия атрибута от прямого доступа.
        self._model = model
        self._year_of_release = year_of_release

    def power_on(self) -> None:
        """
        Метод, представляющий включение устройства.
        """
        print(f"{self._brand} {self._model} включено.")

    def __str__(self) -> str:
        """
        Магический метод для представления объекта в виде строки.
        """
        return f"{self._brand} {self._model} ({self._year_of_release})"

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки, используемой для отладки.
        """
        return f"Device(brand={self._brand}, model={self._model}, year_of_release={self._year_of_release})"


class Smartphone(Device):
    """Дочерний класс Смартфон."""

    def __init__(self, brand: str, model: str, year_of_release: int, os: str):
        """
        Конструктор класса Смартфон.

        Args:
            brand (str): Бренд смартфона.
            model (str): Модель смартфона.
            year_of_release (int): Год выпуска смартфона.
            os (str): Операционная система смартфона.
        """
        super().__init__(brand, model, year_of_release)
        self._os = os  # Используем инкапсуляцию для скрытия атрибута от прямого доступа.

    def make_call(self, number: str) -> None:
        """
        Метод для осуществления звонка.

        Args:
            number (str): Номер телефона для звонка.
        """
        print(f"Вызываем {number} с помощью {self._brand} {self._model}.")

    # Перегрузка метода power_on для смартфона
    def power_on(self) -> None:
        """
        Метод, представляющий включение смартфона, с расширением базового метода.
        """
        super().power_on()
        print(f"Инициализация {self._os}...")

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки, используемой для отладки.
        """
        return f"Smartphone(brand={self._brand}, model={self._model}, year_of_release={self._year_of_release}, os={self._os})"


class Laptop(Device):
    """Дочерний класс Ноутбук."""

    def __init__(self, brand: str, model: str, year_of_release: int, screen_size: float):
        """
        Конструктор класса Ноутбук.

        Args:
            brand (str): Бренд ноутбука.
            model (str): Модель ноутбука.
            year_of_release (int): Год выпуска ноутбука.
            screen_size (float): Размер экрана ноутбука в дюймах.
        """
        super().__init__(brand, model, year_of_release)
        self._screen_size = screen_size  # Используем инкапсуляцию для скрытия атрибута от прямого доступа.

    def open_lid(self) -> None:
        """Метод для открытия крышки ноутбука."""
        print(f"Открываем крышку {self._brand} {self._model}.")

    # Перегрузка метода power_on для ноутбука
    def power_on(self) -> None:
        """
        Метод, представляющий включение ноутбука, с расширением базового метода.
        """
        super().power_on()
        print(f"Загрузка операционной системы...")

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки, используемой для отладки.
        """
        return f"Laptop(brand={self._brand}, model={self._model}, year_of_release={self._year_of_release}, screen_size={self._screen_size})"
