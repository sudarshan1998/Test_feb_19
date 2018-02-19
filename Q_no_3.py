#Create a Student class and initialize it with name and roll number. Make methods to :
      #a. Display - It should display all informations of the student.
      #b. setAge - It should assign age to student
      #c. setMarks - It should assign marks to the student.


class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def setAge(self,age):
        self.age=age

    def setMarks(self,marks):
        self.marks=marks

obj=Student("sudarshan",645)
print(obj.__dict__)
Student.setAge(obj,46)
print(obj.age)
Student.setMarks(obj,90)
print(obj.marks)
print(obj.__dict__)


