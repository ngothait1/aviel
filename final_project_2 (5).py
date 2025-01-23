def printMenu():
    menu = ["1. Save a new entry  ","2. search by ID  ", "3. Print ages average ", "4. Print all names ", "5. Print all IDs ", "6. Print all entries ", "7. Print entry by index ", "8. Exit " ]
    for option in menu:
       print(option)
    
def saveNewEntry(people_dict):
      all_members = 0
      person = input("ID: " )
      if person.isdigit() == True:
          person = int(person)
      else:
            print("Error: ID must be a number " + person + " is not anumber")
            input("Prees Enter to continue ")
      printMenu()
      input("Please enter your chouce: ")

      name = input("name: ")
      age = input("age: " )
      people_dict[person] = {"Name" : name, "Age: " : age}
      all_members += 1
      return people_dict

# def searchById():

# def printAgesAverage():

# def printAllNames():

# def printAllIds():

# def printAllEntries():

# def printEntryByIndex():



people_dict = {}
saveNewEntry(people_dict)


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
      









