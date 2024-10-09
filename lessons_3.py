# 1. Создать класс Computer с приватными атрибутами cpu и memory
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # 2. Добавить сеттеры и геттеры к существующим атрибутам
    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    # 3. Метод make_computations, выполняющий арифметические вычисления с атрибутами cpu и memory
    def make_computations(self):
        return self.__cpu * self.__memory

    # 9. Переопределение __str__ для вывода информации об объекте
    def __str__(self):
        return f"Computer with CPU: {self.__cpu} GHz and Memory: {self.__memory} GB"

    # 10. Переопределение магических методов для сравнения по memory
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


# 4. Создать класс Phone с приватным полем sim_cards_list
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # 5. Сеттеры и геттеры для sim_cards_list
    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # 6. Метод call для симуляции звонка
    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Некорректный номер сим-карты.")

    # 9. Переопределение __str__ для вывода информации об объекте
    def __str__(self):
        return f"Phone with SIM cards: {', '.join(self.__sim_cards_list)}"


# 7. Создать класс SmartPhone, наследуемый от Computer и Phone
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # 8. Метод use_gps для симуляции построения маршрута
    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    # 9. Переопределение __str__ для вывода информации об объекте
    def __str__(self):
        return f"SmartPhone with CPU: {self.get_cpu()} GHz, Memory: {self.get_memory()} GB and SIM cards: {', '.join(self.get_sim_cards_list())}"


# 11. Создать объекты
computer = Computer(3.5, 16)
phone = Phone(["Beeline", "Megafon", "O!"])
smartphone1 = SmartPhone(2.8, 8, ["Beeline", "O!"])
smartphone2 = SmartPhone(3.2, 12, ["Megafon"])

# 12. Распечатать информацию о созданных объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# 13. Опробовать методы
print(f"Вычисления на компьютере: {computer.make_computations()}")

phone.call(1, "+996 777 99 88 11")
phone.call(4, "+996 777 99 88 12")  # Для проверки некорректного номера

smartphone1.use_gps("ЦУМ")
print(f"Вычисления на смартфоне: {smartphone1.make_computations()}")

# Магические методы сравнения
print(smartphone1 == smartphone2)
print(smartphone1 < smartphone2)
