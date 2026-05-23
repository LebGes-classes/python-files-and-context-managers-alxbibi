import ProductCard as pc
from decimal import Decimal


class Menu:
    """Класс для описания пользовательского меню"""

    def __init__(self, chosen_product: pc.ProductCard = None, products_dict: dict = None) -> None:
        """Инициализация класса

        Args:
            chosen_product: выбранная карточка товара
            products_dict: словарь всех карточек товаров
        """

        self.__chosen_product = chosen_product
        self.__products_dict = products_dict

    def get_products_dict(self):
        """Геттер для словаря карточек товаров

        Returns:
            products_dict: словарь всех карточек товаров
        """

        return self.__products_dict

    def show_main_menu(self) -> None:
        """Метод для отрисовки главного меню"""

        product_id = 'Нет'
        if self.__chosen_product:
            product_id = self.__chosen_product.get_id()

        print(
            f'\nГлавное меню. Выберите товар и команду. Выбранный товар: {product_id}\n',
            '0. Сохранить и выйти\n',
            '1. Изменить характеристику товара\n',
            '2. Получить одну характеристику товара\n',
            '3. Получить все характеристики товара\n',
            '4. Посмотреть все товары\n',
            '5. Выбрать другой товар\n',
            '6. Создать карточку товара\n'
        )

    def show_setters_menu(self) -> None:
        """Метод для отрисовки меню сеттеров"""

        product_id = 'Нет'
        if self.__chosen_product:
            product_id = self.__chosen_product.get_id()

        print(
            f'\nМеню для редактирования характеристик товара. Выберите команду. Выбранный товар: {product_id}\n',
            '1. Изменить ID\n',
            '2. Изменить название\n',
            '3. Изменить количество\n',
            '4. Изменить поставщика\n',
            '5. Изменить производителя\n',
            '6. Изменить стоимость\n',
            '7. Изменить местоположение\n',
            '8. Изменить город\n',
            '9. Изменить состояние\n',
            '0. Вернуться в главное меню\n'
        )

    def show_getters_menu(self) -> None:
        """Метод для отрисовки меню геттеров"""

        product_id = 'Нет'
        if self.__chosen_product:
            product_id = self.__chosen_product.get_id()

        print(
            f'\nМеню для получения информации о товаре. Выберите команду. Выбранный товар: {product_id}\n',
            '1. Получить ID\n',
            '2. Получить название\n',
            '3. Получить количество\n',
            '4. Получить поставщика\n',
            '5. Получить производителя\n',
            '6. Получить стоимость\n',
            '7. Получить местоположение\n',
            '8. Получить город\n',
            '9. Получить состояние\n',
            '0. Вернуться в главное меню\n'
        )

    def setters_menu_logic(self, is_running=False) -> bool:
        """Метод для работы меню сеттеров

        Args:
            is_running: флаг вызова меню

        Returns:
            is_running: флаг вызова меню
        """

        while is_running:
            self.show_setters_menu()

            choice = int(input('Введите ваш выбор:'))

            match choice:
                case 0:
                    self.main_menu_logic(is_running)
                    is_running = False
                case 1:
                    id = input('Введите ID: ')
                    self.__chosen_product.set_id(id)
                case 2:
                    name = input('Введите название: ')
                    self.__chosen_product.set_name(name)
                case 3:
                    count = int(input('Введите количество: '))
                    self.__chosen_product.set_count(count)
                case 4:
                    provider = input('Введите поставщика: ')
                    self.__chosen_product.set_provider(provider)
                case 5:
                    manufacturer = input('Введите производителя: ')
                    self.__chosen_product.set_manufacturer(manufacturer)
                case 6:
                    cost = Decimal(input('Введите цену: '))
                    self.__chosen_product.set_cost(cost)
                case 7:
                    location = input('Введите местоположение: ')
                    self.__chosen_product.set_location(location)
                case 8:
                    city = input('Введите город: ')
                    self.__chosen_product.set_city(city)
                case 9:
                    state = input('Введите состояние: ')
                    self.__chosen_product.set_state(state)

        return is_running

    def getters_menu_logic(self, is_running=False) -> bool:
        """Метод для работы меню геттеров

        Args:
            is_running: флаг вызова меню

        Returns:
            is_running: флаг вызова меню
        """

        while is_running:
            self.show_getters_menu()

            choice = int(input('Введите ваш выбор:'))

            match choice:
                case 0:
                    self.main_menu_logic(is_running)
                    is_running = False
                case 1:
                    print(self.__chosen_product.get_id())
                case 2:
                    print(self.__chosen_product.get_name())
                case 3:
                    print(self.__chosen_product.get_count())
                case 4:
                    print(self.__chosen_product.get_provider())
                case 5:
                    print(self.__chosen_product.get_manufacturer())
                case 6:
                    print(self.__chosen_product.get_cost())
                case 7:
                    print(self.__chosen_product.get_location())
                case 8:
                    print(self.__chosen_product.get_city())
                case 9:
                    print(self.__chosen_product.get_state())

        return is_running

    def main_menu_logic(self, is_running=False) -> bool:
        """Метод для работы меню сеттеров

        Args:
            is_running: флаг вызова меню

        Returns:
            is_running: флаг вызова меню
        """

        while is_running:
            self.show_main_menu()

            choice = int(input('Введите ваш выбор:'))

            match choice:
                case 0:
                    is_running = False
                case 1:
                    self.setters_menu_logic(is_running)
                case 2:
                    self.getters_menu_logic(is_running)
                case 3:
                    self.__chosen_product.show_info()
                case 4:
                    for product in self.__products_dict.values():
                        print(product.show_info())
                case 5:
                    chosen_product_id = input('Введите ID товара: ')
                    self.__chosen_product = self.__products_dict[chosen_product_id]
                case 6:
                    product = pc.ProductCard()
                    id = input('Введите id: ')
                    name = input('Введите название: ')
                    count = int(input('Введите количество: '))
                    provider = input('Введите поставщика: ')
                    manufacturer = input('Введите производителя: ')
                    cost = Decimal(input('Введите цену: '))
                    location = input('Введите местоположение: ')
                    city = input('Введите город: ')
                    state = input('Введите состояние: ')
                    product.set_id(id)
                    product.set_name(name)
                    product.set_count(count)
                    product.set_provider(provider)
                    product.set_manufacturer(manufacturer)
                    product.set_cost(cost)
                    product.set_location(location)
                    product.set_city(city)
                    product.set_state(state)
                    self.__products_dict[product.get_id()] = product

        return is_running
