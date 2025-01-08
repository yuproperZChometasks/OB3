"""
Вот пример реализации вашего задания на Python, с выводом на русском языке:
"""

import json

# Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Некоторый звук"

    def eat(self):
        return f"{self.name} ест."

# Подкласс Bird
class Bird(Animal):
    def make_sound(self):
        return "Чирик"

    def fly(self):
        return f"{self.name} летит."

# Подкласс Mammal
class Mammal(Animal):
    def make_sound(self):
        return "Рррр"

    def run(self):
        return f"{self.name} бежит."

# Подкласс Reptile
class Reptile(Animal):
    def make_sound(self):
        return "Шшш"

    def crawl(self):
        return f"{self.name} ползет."

# Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")

# Базовый класс Employee
class Employee:
    def __init__(self, name):
        self.name = name

# Подкласс ZooKeeper
class ZooKeeper(Employee):
    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."

# Подкласс Veterinarian
class Veterinarian(Employee):
    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."

# Класс Zoo
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
if __name__ == "__main__":
    zoo = Zoo()

    # Добавляем животных
    zoo.add_animal(Bird("Кеша", 2))
    zoo.add_animal(Mammal("Лео", 5))
    zoo.add_animal(Reptile("Снэйк", 3))

    # Добавляем сотрудников
    zoo.add_employee(ZooKeeper("Алиса"))
    zoo.add_employee(Veterinarian("Боб"))

    # Вызываем звук животных
    animal_sound(zoo.animals)

    # Сохраняем зоопарк в файл
    zoo.save_to_file('zoo_data.json')

    # Загружаем зоопарк из файла
    new_zoo = Zoo()
    new_zoo.load_from_file('zoo_data.json')

    # Проверяем загруженные данные
    print("\nЗагруженные животные:")
    animal_sound(new_zoo.animals)

"""
### Объяснение кода:
1. **Класс `Animal`**: Базовый класс для всех животных, содержащий общие атрибуты и методы, такие как `make_sound()` и 
`eat()`.
2. **Подклассы `Bird`, `Mammal`, `Reptile`**: Эти классы наследуют от `Animal` и переопределяют метод `make_sound()` для 
специфичных звуков.
3. **Функция `animal_sound()`**: Эта функция принимает список животных и вызывает метод `make_sound()` для каждого из них, 
демонстрируя полиморфизм.
4. **Класс `Zoo`**: Использует композицию для хранения информации о животных и сотрудниках. Включает методы для добавления 
животных и сотрудников, а также для сохранения и загрузки данных из файла.
5. **Классы `ZooKeeper` и `Veterinarian`**: Эти классы представляют сотрудников зоопарка и содержат методы для кормления и 
лечения животных.
6. **Сохранение и загрузка данных**: Реализованы методы для сохранения информации о зоопарке в JSON файл и загрузки из 
него, что обеспечивает "постоянное состояние" между запусками программы.
Этот код предоставляет полную реализацию вашего задания с выводом на русском языке.
"""