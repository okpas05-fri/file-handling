# 
# Error handling

# x = 10
# if x > 5:
#     raise ValueError("sillys")

# indexerror:

# nums = [10, 20, 30, 40]
# idx = int(input("Enter an index: "))
# try:
# print(nums[idx])
# except IndexError:
#  print("list index is out of control.")
# else:
#  print("All was ok.") # only runs, when no exception is caught
# finally:
#  print("Am always here!") # Always runs!!

# handling specific Errors:

# a = 50
# b = 10 
# try:
#  print(a / b)
#  print(c)
# except ZeroDivisionError:
#  print("zero divide error!")
# except NameError:
#  print("Name error!")
 
#a = 50
# b = 0 
# try:
#  print(a / b)
#  print(c)
# except ZeroDivisionError:
#  print("zero divide error!")
# except NameError:
#  print("Name error!")

# typeError
# a = "10"
# b = 10
# try:
#  print(a + b)
# except TypeError as error:
#  print("Type error! has occure.")
#  print(error)

# ValueError
# a = "ten"
# b = 10
# try:
#  print(int(a))
# except ValueError as error:
#  print(error)

# IndexError

# def access_index(string : str, idx : int)-> str:
#  try:
#   return string[idx]
#  except IndexError:
#   return string[0]
 
# print(access_index("Banana",20))


# keyError

# names = ["John", "Peter"]
# ages = (78, 56)
# names_ages = dict(zip(names, ages))
# try:
#  print(names_ages["james"])
# except KeyError:
#  print("key is not here.")


# age = "seventy"
# try:
#  print(int(age))
# except ValueError:
#  print("please type your age in numbers")

# age = "seventy"
# name = "friday"
# # NameError, ValueError, IndexError, TypeError, ZerodivisionError, keyError
# # alias = as name
# a = 10
# b = 0

# try:
#      print(a/b)
#      print(name[9])
#      print(int(age))
#      print(last_name)
# except NameError as error:
#        print("please fill in your last name")
#        print("error")
# except IndexError:
#       print("The number is out of range")
# except ValueError:
#       print("please type your age in numbers")
# except ZeroDivisionError:
#       print("dividing by zero is not possible")
# else:
#       print("this will show if there is no error")
# finally:
#       print("This will always run")

# import random as rand

# number = rand.randint(3, 7)
# number = rand.uniform(3, 7)

# print(number)

# cars = ["bmw", "benz", "toyoya", "volvl"]
# rand.shuffle(cars)
# print(cars)
# our_choice = rand.choice(cars)
# print(our_choice)

