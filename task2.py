#Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
#Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal 
#и добавляют дополнительные атрибуты

import logging

logging.basicConfig(level=logging.INFO, filename="file2.log",filemode="a", format="%(asctime)s %(levelname)s %(message)s")

class Animal:
    def new(cls, *args, **kwargs):
        return super().new(cls)
     
    def __init__(self, name):
        self.name = name

class Bird(Animal):    
    def __init__(self, name, wingspan):
        super().init(name)
        logging.info(f"Имя животного: {name}")
        self.wingspan = wingspan
        self.wing_length()

    def wing_length(self):
        l = self.wingspan / 2
        logging.info(f"Длина крыла: {l}")
        return l

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        logging.info(f"Имя животного: {name}")
        self.max_depth = max_depth
        self.depth()

    def depth(self):
        if self.max_depth < 10:
            logging.info("Мелководная рыба")
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            logging.info("Глубоководная рыба")
            return 'Глубоководная рыба'
        logging.info("Средневодная рыба")
        return 'Средневодная рыба'

class Mammal(Animal):
    def __init__(self, name, weight):
        super().init(name)
        logging.info(f"Имя животного: {name}")
        self.weight = weight
        self.category()

    def category(self):
        if self.weight < 1:
            logging.info("Малявка")
            return 'Малявка'
        elif self.weight > 200:
            logging.info("Гигант")
            return 'Гигант'
        logging.info("Обычный вес")
        return 'Обычный вес'

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == 'Bird':
            return Bird(*args)
        elif animal_type == 'Fish':
            return Fish(*args)
        elif animal_type == 'Mammal':
            return Mammal(*args)
        else:
            logging.error("Недопустимый тип животного")
            raise ValueError('Недопустимый тип животного')

typeAnimal = input('Введите тип животного: ')
nameAnimal = input('Введите имя животного: ')
weightAnimal = int(input('Введите вес животного: '))
result = AnimalFactory.create_animal(typeAnimal, nameAnimal, weightAnimal)