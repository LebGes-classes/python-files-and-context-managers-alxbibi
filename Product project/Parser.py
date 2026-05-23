from abc import ABC, abstractmethod
import json
from ProductCard import *


class BaseSerializer(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass


class BaseDeserializer(ABC):
    @abstractmethod
    def deserialize(self):
        pass


class TxtParser(BaseDeserializer):

    def __init__(self, txt_data_file: str = 'data.txt') -> None:
        """Инициализация класса

        Args:
            txt_data_file: txt файл с данными
        """

        self.__txt_data_file = txt_data_file

    def deserialize(self) -> dict:
        """Метод десериализации txt

        Returns:
            products: словарь формата id: экземпляр ProductCard
        """

        products = list()
        products_dict = dict()
        keys = ['id', 'Наименование', 'Количество', 'Состояние', 'Поставщик', 'Производитель', 'Стоимость', 'Местоположение', 'Город']

        with open(self.__txt_data_file, 'r', encoding='utf-8') as file:
            file.readline()

            for line in file:
                products.append(dict(zip(keys, line.split(';')[1:])))
                products[-1]['Количество'] = int(products[-1]['Количество'])
                products[-1]['Стоимость'] = Decimal(products[-1]['Стоимость'].split()[0])

        for i in range(len(products)):
            new_card = ProductCard().from_dict(products[i])
            products_dict[new_card.get_id()] = new_card

        return products_dict


class JsonParser(BaseDeserializer, BaseSerializer):

    def __init__(self, json_data_file: str = 'database.json') -> None:
        """Инициализация класса

        Args:
            json_data_file: json файл с данными
        """

        self.__json_data_file = json_data_file

    def deserialize(self) -> dict:
        """Метод десериализации json

        Returns:
            products: список экземпляров ProductCard
        """

        products = dict()

        with open(self.__json_data_file, 'r', encoding='utf-8') as file:
            cards = json.load(file)
            for id, card in cards.items():
                products[id] = ProductCard().from_dict(card)

        return products

    def serialize(self, products: dict) -> None:
        """Метод сериализации в json

        Args:
            products: список экземпляров ProductCard
        """

        for id, product in products.items():
            products[id] = product.to_dict()

        with open(self.__json_data_file, 'w', encoding='utf-8') as file:
            json.dump(products, file, ensure_ascii=False, indent=4)
