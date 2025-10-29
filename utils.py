def getNumber(param = None):
    while True:
      user_input = input("Please enter your " + param + ":")
      if user_input.isdigit() == True:
           user_input = int(user_input)
           return user_input
      print(param +" must be a number")
