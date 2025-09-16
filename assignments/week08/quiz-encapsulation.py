class Rectangle:

    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def getArea(self,):
        area = self.__length * self.__width
        return f"Area = {area}"

    def getPerimeter(self,):
        perimeter = 2 * (self.__length + self.__width)
        return f"Perimeter = {perimeter}"
        
    def isSquare(self):
        if self.__length == self.__width:
            return f"This rectangle is square"
        else:
            return f"This rectangle is not square"
        
rectangle = Rectangle(10,5)
print(rectangle.getArea())
rectangle.getPerimeter()
print(rectangle.isSquare())