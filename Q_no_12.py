# Create a SquareGeometry class which takes in length as initialize parameter.
# Make two methods getArea and getPerimeter inside this class. Which when invoked
# returns area and perimeter of each square instance

class SquareGeometry:
    def __init__(self,length):
        self.length=length

    def getArea(self):
        return self.length**2

    def getPerimeter(self):
        return self.length*4

obj=SquareGeometry(67)
print(obj.getArea())
print(obj.getPerimeter())

