class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


rect = Rectangle(float(input("enter length")), float(input("enter width")))


print("Square:", rect.area())
print("Perimeter:", rect.perimeter())
