from collections import namedtuple
from typing import List


original_example = [
    ("Ноутбук", 1500, "Татьяна", "89002001020"),
    ("Смартфон", 500, "Анна", "89202202325"),
    ("Проектор", 300, "Андрей", "89505205656"),
    ("Принтер", 750, "Игорь", "89303303236"),
    ("Планшет", 2300, "Игорь", "89303303236"),
    ("Смартфон", 1000, "Андрей", "89505205656"),
    ("Ноутбук", 4800, "Татьяна", "89002001020"),
    ("Наушники", 780, "Марина", "89562002350"),
    ("Сканер", 550, "Сергей", "89808564559"),
    ("Планшет", 1200, "Анна", "89202202325"),
    ("Ноутбук", 1100, "Игорь", "89303303236"),
    ("Смартфон", 3500, "Татьяна", "89002001020"),
]


class DatabaseKeyExistsError(Exception):
    def __init__(self, key):
        self.message = f"Key {key} is exists!"
        super().__init__(self.message)


class DatabaseKeyNotExistsError(Exception):
    def __init__(self, key):
        self.message = f"Key {key} not exists!"
        super().__init__(self.message)


class Database:
    def __init__(self):
        self.__customers: dict[str, str] = dict()
        self.__repairs: dict[str, dict[int, dict]] = dict()

    def add_customer(self, customer_name: str, customer_phone: str) -> None:
        if customer_phone not in self.__customers:
            self.__customers[customer_phone] = customer_name
            self.__repairs[customer_phone] = dict()
        else:
            raise DatabaseKeyExistsError(customer_phone)

    def get_customer_name_from_phone(self, customer_phone) -> str | None:
        if customer_phone in self.__customers:
            return self.__customers[customer_phone]
        else:
            raise DatabaseKeyNotExistsError(customer_phone)

    def add_repair_for_customer(
        self, customer_phone: str, repair_name: str, repair_price: float
    ) -> None:
        if customer_phone in self.__customers:
            index = len(self.__repairs[customer_phone])
            self.__repairs[customer_phone].update(
                {index: {"repair_name": repair_name, "repair_price": repair_price}}
            )
        else:
            raise DatabaseKeyNotExistsError(customer_phone)

    def get_repair_for_customer(self, customer_phone: str) -> dict:
        if customer_phone in self.__customers:
            customer_name = self.get_customer_name_from_phone(customer_phone)
            repairs = str()
            for index in self.__repairs[customer_phone]:
                repairs += f"{self.__repairs[customer_phone][index]['repair_name']} - {self.__repairs[customer_phone][index]['repair_price']}; "
            return f"{customer_name} {customer_phone}: {repairs}"
        else:
            raise DatabaseKeyNotExistsError(customer_phone)

    def populate_db(self, data: list[tuple]):
        for row in data:
            repair_name = row[0]
            repair_price = row[1]
            customer_name = row[2]
            customer_phone = row[3]

            try:
                self.add_customer(customer_name, customer_phone)
                self.add_repair_for_customer(customer_phone, repair_name, repair_price)
            except DatabaseKeyExistsError:
                self.add_repair_for_customer(customer_phone, repair_name, repair_price)
