from Person import Person
from utils import getnumber
class Employee(Person):
    def __init__(self):
        super().__init__()
        self._salary = getnumber("salary")
        self._field_of_work = input("field_of_work")


    def getFieldOfWork(self):
        return self._field_of_work    
    
    def getSalary(self):
        return self._salary
    
    def printEmployee(self):
        self.printPerson()
        print("The filed of work is " + self.getFieldOfWork() + ", the salary is " + str(self.getSalary))

    def __repr__(self):
        return super().__repr__() + "the salary is " + str(self.getSalary()) + " The filed of work is " + self.getFieldOfWork()

def getnumber(param = None):
    while True:
      user_input = input("Please enter your " + param + ":")
      if user_input.isdigit() == True:
           user_input = int(user_input)
           return user_input
      print(param +" must be a number")



if __name__ == "__main__":
   new_employee = Employee()
   print(new_employee)





