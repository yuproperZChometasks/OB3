"""
Задание. Запрограммировать на питоне
1. Создайте базовый класс Animal, который будет содержать общие атрибуты (например, name, age) и методы (make_sound(), 
eat()) для всех животных.
2. Реализуйте наследование, создав подклассы Bird, Mammal, и Reptile, которые наследуют от класса Animal. Добавьте 
специфические атрибуты и переопределите методы, если требуется (например, различный звук для make_sound()).
3. Продемонстрируйте полиморфизм: создайте функцию animal_sound(animals), которая принимает список животных и вызывает 
метод make_sound() для каждого животного.
4. Используйте композицию для создания класса Zoo, который будет содержать информацию о животных и сотрудниках. Должны быть 
методы для добавления животных и сотрудников в зоопарк.
5. Создайте классы для сотрудников, например, ZooKeeper, Veterinarian, которые могут иметь специфические методы (например, 
feed_animal() для ZooKeeper и heal_animal() для Veterinarian).
Дополнительно:
Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

Вот пример реализации задания на Python:
"""

import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some sound"

    def eat(self):
        return f"{self.name} is eating."


class Bird(Animal):
    def make_sound(self):
        return "Chirp"

    def fly(self):
        return f"{self.name} is flying."


class Mammal(Animal):
    def make_sound(self):
        return "Roar"

    def run(self):
        return f"{self.name} is running."


class Reptile(Animal):
    def make_sound(self):
        return "Hiss"

    def crawl(self):
        return f"{self.name} is crawling."


def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} says: {animal.make_sound()}")


class Employee:
    def __init__(self, name):
        self.name = name


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        return f"{self.name} is feeding {animal.name}."


class Veterinarian(Employee):
    def heal_animal(self, animal):
        return f"{self.name} is healing {animal.name}."


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        data = {
            'animals': [{'name': animal.name, 'age': animal.age, 'type': animal.__class__.__name__} for animal in self.animals],
            'employees': [{'name': employee.name, 'type': employee.__class__.__name__} for employee in self.employees]
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for animal_data in data['animals']:
                if animal_data['type'] == 'Bird':
                    animal = Bird(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Mammal':
                    animal = Mammal(animal_data['name'], animal_data['age'])
                elif animal_data['type'] == 'Reptile':
                    animal = Reptile(animal_data['name'], animal_data['age'])
                self.add_animal(animal)

            for employee_data in data['employees']:
                if employee_data['type'] == 'ZooKeeper':
                    employee = ZooKeeper(employee_data['name'])
                elif employee_data['type'] == 'Veterinarian':
                    employee = Veterinarian(employee_data['name'])
                self.add_employee(employee)


# Пример использования

zoo = Zoo()

# Добавляем животных
zoo.add_animal(Bird("Tweety", 2))
zoo.add_animal(Mammal("Leo", 5))
zoo.add_animal(Reptile("Kaa", 3))

# Добавляем сотрудников
zoo.add_employee(ZooKeeper("Alice"))
zoo.add_employee(Veterinarian("Bob"))

# Вызываем звук животных
animal_sound(zoo.animals)

# Сохраняем зоопарк в файл
zoo.save_to_file('zoo_data.json')

# Загружаем зоопарк из файла
new_zoo = Zoo()
new_zoo.load_from_file('zoo_data.json')

# Проверяем загруженные данные
animal_sound(new_zoo.animals)

"""
### Объяснение кода:

1. **Класс `Animal`**: Базовый класс для всех животных, содержащий общие атрибуты и методы.
2. **Подклассы `Bird`, `Mammal`, `Reptile`**: Реализация наследования, каждая из которых переопределяет метод `make_sound()` 
для специфичных звуков.
3. **Функция `animal_sound()`**: Демонстрация полиморфизма, принимает список животных и вызывает для каждого метод 
`make_sound()`.
4. **Класс `Zoo`**: Использует композицию для хранения информации о животных и сотрудниках. Методы для добавления животных 
и сотрудников, а также для сохранения и загрузки информации в файл.
5. **Классы `ZooKeeper` и `Veterinarian`**: Специфические классы для сотрудников зоопарка с методами для кормления и лечения 
животных.

Этот код обеспечивает основную функциональность, описанную в задании, и может быть дополнительно расширен по мере 
необходимости.
"""