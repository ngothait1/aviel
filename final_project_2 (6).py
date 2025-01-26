def printMenu():
    menu = ["1. Save a new entry  ","2. search by ID  ", "3. Print ages average ", "4. Print all names ", "5. Print all IDs ", "6. Print all entries ", "7. Print entry by index ", "8. Exit " ]
    for option in menu:
       print(option)
    input("Please enter your chouce: ")


def saveNewEntry(people_dict):
      all_members = 0
      person = input("ID: " )
      if person.isdigit() == True:
         person = int(person)
      else:
          return print("Error: ID must be a number " + person + " is not anumber")
      name = input("name: ")
      age = input("age: " )
      if age.isdigit() == True:
         age = int(age)
         return print("Error: Age must be a number " + str(age) + "is not number" )  
      people_dict[person] = {"Name" : name, "Age: " : age}
      all_members += 1
      return people_dict

def searchById(people_dict,ID ):
   input ("Please enter the ID you want to look for:  ")
   if ID in people_dict:
        return people_dict[ID]
   else:
        return "The key " + ID + " does not exist"


# def printAgesAverage():

# def printAllNames():

# def printAllIds():

# def printAllEntries():

# def printEntryByIndex():


people_dict = {}
all_members = ()
saveNewEntry(people_dict)
# printMenu()
print(all_members)


# printMenu()
# choice = input("Please enter your chouce: ")

# while True:
#    printMenu()
#    choice = input("Please enter your chouce: ")
#    if choice == "1":
#       saveNewEntry()
#    elif
#       choice == "2"
#       printAgesAverage()
#    elif
#       choice == "3":
#       printAllNames()
#    elif
#       choice == "4"
#       printAllNames()
#    elif
#       choice == "5"
#       printAllIds()
#    elif
#       choice == "6"
#       printAllEntries()
#    elif
#       choice == "7"
#       printEntryByIndex()
#    elif
#       choice == "8"
#       exit = input("Are you sure? (y/n) ")
#       if exit == "y":
#          print( "Goodbye !" )
#       elif
#          exit == "n"
#          printMenu()
#       continue
      









