def printMenu():
    menu = ["1. Save a new entry",
     "2. search by ID",
     "3. Print ages average",
     "4. Print all names",
     "5. Print all IDs",
     "6. Print all entries",
     "7. Print entry by index",
     "8. Exit"]
    for option in menu:
       print(option)
    
def getnumber(parame = None):
   char = input("Please enter your" + parame + ":")
   while char.isdigit() == False:
     print(parame +"must be a number")
     char = input("Please enter your" + parame + ":")
   else:
      char = int(char)
      return char

def saveNewEntry(people_dict, age_sum):
   user_id = getnumber("ID")
   name = input("name: ")
   age = getnumber("ege")
   people_dict[user_id] = {"Name" : name, "Age: " : age}
   print("ID" + people_dict[user_id] + "save suceessfuly")
   age_sum += age
   return age_sum

def searchById(people_dict):
   user_id = input("Please enter the ID you want to look for: ")
   if user_id.isdigit() == True:
      user_id = int(user_id)
   else:
      print("Error: ID must be a number " + user_id + " is not anumber")
      return 

   if user_id in people_dict:
      print(people_dict[user_id])
   else:
      print("The key " + user_id + " does not exist")

def printAgesAverage(people_dict,age_sum):
   if len(people_dict) == 0:
      print(0)
   else:   
      print(age_sum / len(people_dict))

def printAllNames():
   for value in people_dict.items():
       print(value["Name"])

def printAllIds(people_dict):
   for key in people_dict.items():
      print(key)

def printAllEntries(people_dict):
    for key, value in people_dict.items():
      print(key + ": " + str(value))

def printEntryByIndex(people_dict):
   index = input("please enter the index of the entry you want to print: ")
   people_list = list(people_dict.items())
   if 0 <= index < len(people_list):
        key, value = people_list[index]
        print("ID:   " + str(key))
        print("Name: " + value["Name"])
        print("Age:  " + str(value["Age: "]))
   else:
        print("Invalid index. Please enter a valid index.")

people_dict = {}
age_sum = 0
while True:
   printMenu()
   choice = input("Please enter your chouce: ")
   if choice == "1":
      age_sum = saveNewEntry(people_dict, age_sum)
   elif choice == "2":
      searchById(people_dict)
   elif choice == "3":
      printAgesAverage(people_dict, age_sum)
   elif choice == "4":
    printAllNames(people_dict)
   elif choice == "5":
    printAllIds(people_dict)
   elif choice == "6":
      printAllEntries(people_dict)
   elif choice == "7":
    printEntryByIndex(people_dict)
   elif choice == "8":
      exit = input("Are you sure? (y/n) ")
      if exit == "y":
         print( "Goodbye !" )
      else:
         exit == "n"
      continue
   input("press enter to continue")      









