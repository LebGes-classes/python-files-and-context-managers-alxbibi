from decimal import Decimal


class GeneralProductCardError(Exception):
    """Класс исключений, возникающих в классе ProductCard"""
    pass


class InvalidDataTypeError(GeneralProductCardError):
    """Исключение, вызываемое при неверном типе введенных данных"""
    pass


class NegativeArgumentError(GeneralProductCardError):
    """Исключение, вызываемое при вводе отрицательного числа"""
    pass


class ProductCard:
    """Класс для описания карточки товара"""

    def __init__(
            self,
            id: str = "None",
            name: str = "None",
            count: int = 0,
            state: str = "None",
            provider: str = "None",
            manufacturer: str = "None",
            cost: Decimal = 0.00,
            location: str = "None",
            city: str = "None"
    ) -> None:
        """Инициализация класса

        Args:
            id: id товара
            name: название товара
            count: количество товара
            state: состояние товара
            provider: поставщик товара
            manufacturer: производитель товара
            cost: цена товара
            location: местоположение товара
            city: город товара
        """

        self.__id = id
        self.__name = name
        self.__count = count
        self.__state = state
        self.__provider = provider
        self.__manufacturer = manufacturer
        self.__cost = cost
        self.__location = location
        self.__city = city

    def set_id(self, id: str) -> None:
        """Сеттер для ID товара

        Args:
            id: ID товара
        """

        self.__id = id

    def set_name(self, name: str) -> None:
        """Сеттер для названия товара

        Args:
            name: название товара
        """

        self.__name = name

    def set_count(self, count: int) -> None:
        """Сеттер для количества товара

        Args:
            count: количество товара
        """

        if count < 0:
            raise ValueError('Количество товара не может быть отрицательным.')

        self.__count = count

    def set_provider(self, provider: str) -> None:
        """Сеттер для поставщика товара

        Args:
            provider: производитель товара
        """

        self.__provider = provider

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер для производителя товара

        Args:
            manufacturer: производитель товара
        """

        self.__manufacturer = manufacturer

    def set_cost(self, cost: Decimal) -> None:
        """Сеттер для стоимости товара

        Args:
            cost: стоимость товара
        """

        if cost < 0:
            raise ValueError('Цена не может быть отрицательной.')

        self.__cost = cost

    def set_location(self, location: str) -> None:
        """Сеттер для местоположения товара

        Args:
            location: местоположение товара
        """

        self.__location = location

    def set_city(self, city: str) -> None:
        """Сеттер для города товара

        Args:
            city: город товара
        """

        self.__city = city

    def set_state(self, state: str) -> None:
        """Сеттер для состояния товара

        Args:
            state: состояние товара
        """

        self.__state = state

    def get_id(self) -> str:
        """Геттер для id товара

        Returns:
            id: id товара
        """

        return self.__id

    def get_name(self) -> str:
        """Геттер для названия товара

        Returns:
            name: название товара
        """

        return self.__name

    def get_count(self) -> int:
        """Геттер для количества товара

        Returns:
            count: количество товара
        """

        return self.__count

    def get_cost(self) -> Decimal:
        """Геттер для стоимости товара

        Returns:
            cost: стоимость товара
        """

        return self.__cost

    def get_location(self) -> str:
        """Геттер для местоположения товара

        Returns:
            location: местоположение товара
        """

        return self.__location

    def get_city(self) -> str:
        """Геттер для города товара

        Returns:
            city: город товара
        """

        return self.__city

    def get_provider(self) -> str:
        """Геттер для поставщика товара

        Returns:
            provider: поставщик товара
        """

        return self.__provider

    def get_manufacturer(self) -> str:
        """Геттер для производителя товара

        Returns:
            manufacturer: производитель товара
        """

        return self.__manufacturer

    def get_state(self) -> str:
        """Геттер для состояния товара

        Returns:
            state: состояние товара
        """

        return self.__state

    def show_info(self) -> None:
        """Вывод значений полей карточки товара"""

        print(f'id: {self.get_id()}, Наименование: {self.get_name()}, Количество: {self.get_count()}, '
              f'Состояние: {self.get_state()}, Поставщик: {self.get_provider()}, Производитель: {self.get_manufacturer()}, '
              f'Стоимость: {self.get_cost()}, Местоположение: {self.get_location()}, Город: {self.get_city()}')

    def show_main_menu(self):
        print('\n Главное меню. Выберите номер команды',
              '1. Изменить характеристику товара',
              '2. Получить характеристику товара',
              '3. Получить всю информацию о товаре'

        )

    def to_dict(self) -> dict:
        """Метод для превращения объекта в словарь

        Returns:
            dicti: словарь полученный из экземпляра
        """

        dicti = dict()

        dicti['id'] = self.__id
        dicti['Наименование'] = self.__name
        dicti['Количество'] = self.__count
        dicti['Состояние'] = self.__state
        dicti['Поставщик'] = self.__provider
        dicti['Производитель'] = self.__manufacturer
        dicti['Стоимость'] = str(self.__cost)
        dicti['Местоположение'] = self.__location
        dicti['Город'] = self.__city

        return dicti

    def from_dict(self, dicti: dict):
        """Метод для превращения словаря в объект

        Args:
            dicti: словарь из которого будет создан экземпляр
        """

        self.set_id(dicti['id'])
        self.set_name(dicti['Наименование'])
        self.set_count(int(dicti['Количество']))
        self.set_state(dicti['Состояние'])
        self.set_provider(dicti['Поставщик'])
        self.set_manufacturer(dicti['Производитель'])
        self.set_cost(Decimal(dicti['Стоимость']))
        self.set_location(dicti['Местоположение'])
        self.set_city(dicti['Город'])

        return self
