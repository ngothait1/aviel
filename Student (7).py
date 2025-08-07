from Person import Person
from utils import getnumber

class Student(Person):
    def __init__(self):
        super().__init__()
        self.field_of_study = input("field_of_study")
        self.year_of_study = getnumber("year_of_study")
        self.score_avg = getnumber("score_avg")

    def getFieldOfStudy(self):
        return self.field_of_study
    
    def getYearOfStudy(self):
        return self.year_of_study
    
    def getScoreAvg(self):
        return self.score_avg
    
    def printStudent(self):
        self.printPerson()
        print("The field of study is " + self.getFieldOfStudy() + " , the year of study " + str(self.getYearOfStudy()) + ", the avg is " + str(self.getScoreAvg()))

    def __repr__(self):
        return super().__repr__() + "The field of study is " + self.getFieldOfStudy() + " , the year of study " + str(self.getYearOfStudy()) + ", the avg is " + str(self.getScoreAvg())


if __name__ == "__main__":
    new_student = Student()
    print(new_student)

    



#     student = Student("yuval", 32, "math", 2000, 78)
#     print(student)

    # field_of_study = input("Please enter the field of study: ")
    # year_of_study = getnumber("year of study")
    # score_avg = getnumber("score avg")



