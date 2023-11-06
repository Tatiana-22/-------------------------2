#В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) 
#имеет следующие атрибуты:
#Фамилия (строка, не пустая) Имя (строка, не пустая) 
#Отчество (строка, не пустая) Возраст (целое положительное число) 
#Сотрудники имеют также уникальный идентификационный номер (ID), 
#который должен быть шестизначным положительным целым числом.
#Ваша задача:
#Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях 
#(Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и генерировать 
#исключения InvalidNameError и InvalidAgeError, если данные неверные.

import logging

logging.basicConfig(level=logging.INFO, filename="file1.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")

class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def str(self):
        logging.error(f"Invalid name: {self.name}. Name should be a non-empty string.")
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def str(self):
        logging.error(f"Invalid age: {self.age}. Age should be a positive integer.")
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(ValueError):
    def __init__(self, id):
        self.id = id

    def str(self):
        logging.error(f"Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.")
        return f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def new(cls, *args, **kwargs):
        return super().new(cls)
    
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            raise InvalidNameError(last_name)
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            raise InvalidNameError(first_name)
        if not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
            raise InvalidNameError(patronymic)
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)

        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        logging.info(f"Person's initials: {self.last_name} {self.first_name} {self.patronymic}")
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1
        logging.info(f"Birthday. Became: {self._age} year")
        

    def get_age(self):
        logging.info(f"Age: {self._age} year")
        return self._age


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, id: int):
        super().init(last_name, first_name, patronymic, age)
        if not isinstance(id, int) or id < 100_000 or id > 999_999:
            raise InvalidIdError(id)

        self.id = id

    def get_level(self):
        s = sum(num for num in str(self.id))
        r = s % self.MAX_LEVEL
        logging.info(f"Уровень: {r}.")
        return r
    
last_name = input('Введите фамилию: ')
first_name = input('Введите имя: ')
patronymic = input('Введите отчество: ')
age = int(input('Введите возраст: '))   

result = Person(last_name, first_name, patronymic, age)

print(result.full_name())
print(result.get_age())
print(result.birthday())
print(result.get_age())


