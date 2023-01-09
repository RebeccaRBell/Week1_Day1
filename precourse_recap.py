first_name = input("What is your first name?")
last_name = input("What is your last name?")
birth_year = input("What year were you born?")
age = (2023 - int(birth_year))


def displayInfo():
    print("Your name is " + first_name + last_name +
          " and you will be " + str(age) + " this year")


displayInfo()
