# Дополнительное практическое задание
# по модулю: "Наследование классов."

# Задание "Они все так похожи":
import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides: int):
        self.__color = [*color] \
            if self.__is_valid_color(*color) \
            else [0, 0, 0]
        self.__sides = [*sides] \
            if len(sides) == self.sides_count \
            else [1] * self.sides_count
        self.filled = False

    def get_color(self):      # возвращает список RGB
        return self.__color

    @staticmethod
    def __is_valid_color( r, g, b):                    # Служебный, принимает параметры r, g, b,
        if (isinstance(x, int)                      # проверяет корректность переданных значений
            and 0 <= x <= 255 for x in (r, g, b)):
            return True
        else:
            return False

    def set_color(self, r, g, b):     # принимает параметры r, g, b и изменяет атрибут __color
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):          # Служебный, принимает кол-во сторон,
        if (len(new_sides) == self.sides_count and   # если число целое и положительное,
            (isinstance(side, int) and side > 0      # кол-во новых сторон совпадает с текущим
            for side in new_sides)):                 # возвращает True, иначе False
                return True
        else:
            return False

    def get_sides(self):        # Возвращает список длин сторон
        return self.__sides
    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):                # Принимает кол-во сторон,
        list_1 = [*new_sides]                       # проверяет корректность переданных данных
        if self.__is_valid_sides(list_1) is True:
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1
   
    def __init__(self, color, *sides: int):
        super().__init__(color, *sides)
        self.__radius = None
        self._radius = self.__len__() / (2 * math.pi)
           
    def get_square(self):
        return math.pi * (self.__radius ** 2)  # Возвращает площадь Круга

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))  # Возвращает площадь треугольника
                                                           # по формулу Герона
    def get_height(self, sides):        # Возвращает высоту треугольника
        a, b, c = self.get_sides()
        side = sides
        if side == "a":
            side = 2 * self.get_square() / a
        elif side == "b":
            side = 2 * self.get_square() / b
        elif side == "c":
            side = 2 * self.get_square() / c
        return side

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        sides = sides * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3# Возвращает объём куба

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
cube2 = Cube((200, 200, 100), 9, 12)
triangle1 = Triangle((122, 35, 234), 10, 15, 18)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube2.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
cube2.set_sides(5, 3, 12, 4, 5) # Изменится
print(cube2.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), высоты треугольника:
print(len(circle1))
#print(triangle1.set_height())

# Проверка объёма (куба):
print(cube1.get_volume())

# Площадь и высота треугольника к сторонам "а, в, с"
print(triangle1.get_square())
print(triangle1.get_height("a"))
print(triangle1.get_height("b"))
print(triangle1.get_height("c"))





