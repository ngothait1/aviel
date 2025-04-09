import json
import pandas as pd
import os
def printMenu():
    menu = ["1. Save a new entry",
     "2. search by ID",
     "3. Print ages average",
     "4. Print all names",
     "5. Print all IDs",
     "6. Print all entries",
     "7. Print entry by index",
     "8. Save all data",
     "9. Exit"]
    for option in menu:
       print(option)
    
def getnumber(param = None):
    while True:
      user_input = input("Please enter your " + param + ":")
      if user_input.isdigit() == True:
           user_input = int(user_input)
           return user_input
      print(param +" must be a number")

def goodPrint(key, value):
      print("ID:   " + str(key))
      print("Name: " + value["Name"])
      print("Age:  " + str(value["Age"]))

def saveNewEntry(people_dict, age_sum, id_list):
   user_id = getnumber("ID")
   if user_id in people_dict:
        print("The ID already exists.")
        return age_sum
   name = input("name: ")
   age = getnumber("age")
   people_dict[user_id] = {"Name" : name, "Age" : age}
   print("ID " + str(user_id) + " save suceessfuly")
   id_list.append(user_id)
   age_sum += age
   return age_sum

def searchById(people_dict):
   user_id = getnumber("ID")
   if user_id in people_dict:
      print(people_dict[user_id])
   else:
      print("The key " + user_id + " does not exist")

def printAgesAverage(people_dict,age_sum):
   if len(people_dict) == 0:
      print(0)
   else:   
      print(age_sum / len(people_dict))

def printAllNames(people_dict):
  for value in people_dict.values():
       print(value["Name"])

def printAllIds(people_dict):
   for key in people_dict.keys():
      print(key)

def printAllEntries(people_dict):
   for key, value in people_dict.items():
      goodPrint(key , value)

def printEntryByIndex(people_dict, id_list):
   index = input("please enter the index of the entry you want to print: ")
   if 0 <= index < len(id_list):
      key = id_list[index]
      value = people_dict[key]
      goodPrint(key, value)
   else:
        print("Invalid index. Please enter a valid index.")

def saveAllData(people_dict):
   conf_path = "C:\\Users\\avielo\\Documents\\learning\\conf.json"
   data_path = "C:\\Users\\avielo\\Documents\\learning\\data.csv"
   if os.path.exists(conf_path):
        with open(conf_path) as conf_file:
            conf = json.load(conf_file)
   else:
        print("Error: config file conf.json is missing in path " + os.getcwd())
        return
   df = pd.DataFrame(people_dict).T # changing the orientation of rows to columns
   df.reset_index(inplace=True) # Includes id as a column
   df.rename(columns={"index": "ID"}, inplace=True)
   fields = ["ID", "Name", "Age"]
   for field in fields:
      df.rename(columns={field: conf[field]}, inplace=True)
   df.to_csv(data_path, index=False)
   print("data save suceessfuly !!!")
people_dict = {}
id_list = []
age_sum = 0
while True:
   printMenu()
   choice = input("Please enter your choice: ")
   if choice == "1":
      saveNewEntry(people_dict, age_sum, id_list)
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
      saveAllData(people_dict)
   elif choice == "9":
      exit = input("Are you sure? (y/n) ")
      if exit == "y":
         print( "Goodbye !" )
         break
      else:
         exit == "n"
         continue
   input("press enter to continue")      









