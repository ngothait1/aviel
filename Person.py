from utils import getNumber
class Person :
    def __init__(self):
        self._name_ = input("name: ")
        self._age_ = getNumber("age")


    def getName(self):
        return self._name_
     

    def getAge(self):
        return self._age_
    

    def printPerson(self):
        print("The person " + self.getName() + " is " + str(self.getAge()) + " years old")


    def __repr__(self):
        return "The person " + self.getName() + " is " + str(self.getAge()) + " years old "
    
    
    def convertToDict(self):
        return { "Name": self.getName(), "Age": self.getAge() }
    


if __name__ == "__main__":
    new_person = Person()
    print(new_person)

    # test_name = "test_name"
    # test_age = 30
    # person = Person(test_name, test_age)
    # if person.getage() != test_age:
    #     print("Error: Age should be " + str(test_age)+ " but i gut " + str(person.getage()))
    # if person.getname() != test_name:
    #     print("Error: Name should be " + str(test_name)+ " but i gut " + str(person.getname())) 

    # print(person) 
        
        