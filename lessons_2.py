# 1-4. Класс Figure
class Figure:
    unit = 'cm'  # единица измерения

    def __init__(self):
        pass  # конструктор без параметров

    def calculate_area(self):
        raise NotImplementedError("Метод должен быть переопределен в подклассе")

    def info(self):
        raise (NotImplementedError("Метод должен быть переопределен в подклассе"))

# 5-8. Класс Square (квадрат)
class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # приватный атрибут

    def calculate_area(self):
        return self.__side_length ** 2  # площадь квадрата

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}")

# 9-12. Класс Rectangle (прямоугольник)
class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  # приватный атрибут длина
        self.__width = width  # приватный атрибут ширина

    def calculate_area(self):
        return self.__length * self.__width  # площадь прямоугольника

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}")

# 13-14. Исполняемый файл
if __name__ == "__main__":
    # Создаем два квадрата и три прямоугольника
    shapes = [
        Square(4), Square(7),  # два квадрата
        Rectangle(5, 10), Rectangle(8, 12), Rectangle(6, 3)  # три прямоугольника
    ]

    # Вызываем метод info для всех объектов
    for shape in shapes:
        shape.info()

# Обьяснение что я сделал:
# 1. Класс Figure содержит два нереализованных метода calculate_area() u info(), которые должны быть переопределены в дочерних классах.
# 2. Класс Square включает приватный атрибут_side_length и методы для вычисления площади и вывода информации.
# 3. Класс Rectangle содержит приватные атрибуты_length u_width u аналогичные методы для площади и информации.
# 4. В конце создается список объектов и через цикл вызывается метод info() для каждого объекта.