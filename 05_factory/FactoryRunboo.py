class Shape:
    def draw(self):
        print("common shape")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")

class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")

class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")

class ShapeFactory():
    def getShape(self, shapeName):
        if shapeName is None:
            return None
        if shapeName is "Circle":
            return Circle()
        elif shapeName is "Rectangle":
            return Rectangle()
        elif shapeName is "Square":
            return Square()

        return None


# FactoryPatternDemo

myFactor = ShapeFactory()

shape1 = myFactor.getShape("Circle")
shape1.draw()

shape2 = myFactor.getShape("Rectangle")
shape2.draw()

shape3 = myFactor.getShape("Rectangle")
shape3.draw()

shape4 = myFactor.getShape("Square")
shape4.draw()







