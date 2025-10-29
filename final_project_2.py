import json
import pandas as pd
import os
from Person import Person
from Student import Student
from employee import Employee
from utils import getNumber


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


def goodPrint(key, value):
   print("ID:   " + str(key))
   print("Name: " + value._name_)
   print("Age:  " + str(value._age_))


def saveNewEntry(people_dict, age_sum, id_list):
   user_id = getNumber("ID")
   class_types = [Person, Student, Employee]
   for index, class_type in enumerate(class_types):
      print(str(index) + ". " + str(class_type.__name__))
   wanted_class = getNumber("choose type")
   if 0 <= wanted_class < len(class_types):
    entry = class_types[wanted_class]()
   else:
      print("The class no exists") 
      return age_sum
   if user_id in people_dict:
      print("The ID already exists.")
      return age_sum
   people_dict[user_id] = entry
   print("ID " + str(user_id) + " save suceessfuly")
   id_list.append(user_id)
   age_sum += entry.getAge()
   return age_sum


def searchById(people_dict):
   user_id = getNumber("ID")
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
      print(value.getName())


def printAllIds(people_dict):
   for key in people_dict.keys():
      print(key)


def printAllEntries(people_dict):
   for index, key in enumerate(people_dict):
      print(str(index) + ".", people_dict[key])


def printEntryByIndex(people_dict, id_list):
   index = int(input("please enter the index of the entry you want to print: "))
   if 0 <= index < len(id_list):
      key = id_list[index]
      value = people_dict[key]
      goodPrint(key, value)
   else:
      print("Invalid index. Please enter a valid index.")


# def saveAllDataOldWithConf(people_dict):
#    conf_path = "C:\\Users\\avielo\\Documents\\learning\\conf.json"
#    filename = input("Please enter the name of the file to save (with .csv extension): ")
#    data_path = os.path.join("C:\\Users\\avielo\\Documents\\learning", filename)
#    if os.path.exists(conf_path):
#         with open(conf_path) as conf_file:
#             conf = json.load(conf_file)
#    else:
#         print("Error: config file conf.json is missing in path " + os.getcwd())
#         return
#    df = pd.DataFrame(people_dict).T # changing the orientation of rows to columns
#    df.reset_index(inplace=True) # Includes id as a column
#    df.rename(columns={"index": "ID"}, inplace=True)
#    fields = ["ID", "Name", "Age"]
#    for field in fields:
#       df.rename(columns={field: conf[field]}, inplace=True)
#    df.to_csv(data_path, index=False)
#    print("data save suceessfuly !!!")



def saveAllData(people_dict):
   filename = input("Please enter the name of the file to save (with .csv extension): ")
   data_path = os.path.join("C:\\Users\\avielo\\Documents\\learning", filename)
   converted_dict = {}
   for key in people_dict.keys():
      converted_dict[key] = people_dict[key].convertToDict()

   df = pd.DataFrame(converted_dict).T # changing the orientation of rows to columns
   df.reset_index(inplace=True) # Includes id as a column
   df.rename(columns={"index": "ID"}, inplace=True)
   df.to_csv(data_path, index=False)
   print("data save suceessfuly !!!")


people_dict = {}
id_list = []
age_sum = 0
while True:
   printMenu()
   choice = input("Please enter your choice: ")
   if choice == "1":
      age_sum = saveNewEntry(people_dict, age_sum, id_list)
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
      printEntryByIndex(people_dict, id_list)
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








