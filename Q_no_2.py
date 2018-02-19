#Create a class Circle which has a class variable PI with value=22/7. Make two methods getArea
# and getCircumference inside this Circle class. Which when invoked returns area and
# circumference of each ciecle instances.

class Circle:
    pi=22/7

    def __init__(self,radius):
        self.radius=radius



    def getArea(self):
        return self.radius**2*Circle.pi

    def getCircumference(self):
        return self.radius*2*Circle.pi

obj=Circle(2)
print(obj.getArea())
print(obj.getCircumference())