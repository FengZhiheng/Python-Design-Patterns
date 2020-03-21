
import abc
#Abstract Base Classes


class Shape(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")

class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")

# class ShapeFactory():
#     def getShape(self, shapeName):
#         if shapeName is None:
#             return None
#         if shapeName is "Circle":
#             return Circle()
#         elif shapeName is "Rectangle":
#             return Rectangle()
#         elif shapeName is "Square":
#             return Square()
#
#         return None


class Color(abc.ABC):
    @abc.abstractmethod
    def fill(self):
        pass

class Red(Color):
    def fill(self):
        print("Inside Red::fill() method.")

class Green(Color):
    def fill(self):
        print("Inside Green::fill() method.")

class Blue(Color):
    def fill(self):
        print("Inside Blue::fill() method.")


class AbstractFactory(metaclass = abc.ABCMeta):
    def getColor(self, color):
        pass
    def getShape(self, shape):
        pass

class ShapeFactory(AbstractFactory):
    def getShape(self, shapeType):
        if shapeType is None:
            return None
        if shapeType is "Circle":
            return Circle()
        elif shapeType is "Rectangle":
            return Rectangle()
        elif shapeType is "Square":
            return Square()

        return None
    def getColor(self, color):
        return None

class ColorFactory(AbstractFactory):
    def getShape(self, shapeType):
        return None
    def getColor(self, color):
        if color is None:
            return None
        if color is "Red":
            return Red()
        elif color is "Green":
            return Green()
        elif color is "Blue":
            return Blue()
        return None

class FactoryProducer():
    @staticmethod
    def getFactory(choice):
        if choice is "Shape":
            return ShapeFactory()
        elif choice is "Color":
            return ColorFactory()
        return None



# AbstractFactoryPatternDemo


shapeFactory = FactoryProducer.getFactory("Shape")
shape1 = shapeFactory.getShape("Circle")
shape1.draw()

shape2 = shapeFactory.getShape("Rectangle")
shape2.draw()

shape3 = shapeFactory.getShape("Square")
shape3.draw()


colorFactory = FactoryProducer.getFactory("Color")
color1 = colorFactory.getColor("Red")
color1.fill()

color2 = colorFactory.getColor("Green")
color2.fill()

color3 = colorFactory.getColor("Blue")
color3.fill()


