from Person import Person
from utils import getNumber


class Employee(Person):
    def __init__(self):
        super().__init__()
        self._salary = getNumber("salary")
        self._field_of_work = input("field of work")


    def getFieldOfWork(self):
        return self._field_of_work    
    

    def getSalary(self):
        return self._salary
    

    def printEmployee(self):
        self.printPerson()
        print("The filed of work is " + self.getFieldOfWork())
        print("the salary is " + str(self.getSalary()))
        

    def __repr__(self):
        return super().__repr__() + "the salary is " + str(self.getSalary()) + " The filed of work is " + self.getFieldOfWork()


    def convertToDict(self):
        info_dict = super().convertToDict() |{ "salary":self.getSalary(),"field of work":self.getFieldOfWork()} 
        return info_dict
 

if __name__ == "__main__":
   new_employee = Employee()
   print(new_employee.convertToDict())





