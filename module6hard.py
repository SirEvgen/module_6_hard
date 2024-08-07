import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.color = list(color)
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [*sides] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.color = (r, g, b)

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            self.__sides = list(new_sides)
        else:
            self.__sides = self.__sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = round(sides[0] / (2 * 3.14159), 2)

    def get_square(self):
        return 2 * 3.14159 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.side = sides[0]
        self.square = round((math.sqrt(3) * self.side ** 2) / 4, 1)
        self.__height = round((self.square / 0.5) / self.side)

    def get_square(self):
        return self.square

    def get_height(self):
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if sides:
            sides = [sides[0]] * self.sides_count
        else:
            sides = [1] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):
        self.length_side = self.get_sides()[0]
        return self.length_side ** 3

    def get_volume_pyramid_of_cube(self):
        length_footing = self.get_sides()[0]
        top = self.length_side
        volume_pyramid = top / 3 * length_footing ** 2
        return volume_pyramid


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 100, 300), 15)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print("Периметр круга")
print(len(circle1))
# Проверка объёма (куба):
print("Объём куба")
print(cube1.get_volume())
print("Площадь треугольника")
print(triangle1.get_square())
print("Высота треугольника (не зря же прописывали для неё вычисления?)")
print(triangle1.get_height())
print("Объём правильной четырёхугольной пирамиды в нашем кубе (это уже от себя)")
print(cube1.get_volume_pyramid_of_cube())
