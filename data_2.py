# print("good morning")

# x = 300
# y = 0

# try:
#     print(x / y)
# except ZeroDivisionError:
#     print("Dividing a number by zero is not possible! ")

# OR

# def divide_number():
#     try:
#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         output = num1 / num2
#         print("Output:", output)
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allow!")
#     except ValueError:
#         print("Error: Invalid input. Please enter a number. ")

# print(divide_number())

# def to_int(john):
#     try:
#         return int(john)
#     except ValueError:
#         return "Invalid integer"
    
# print(to_int("456"))
# print(to_int("john"))

# 3

# our_file = r"C:\Users\C PLUG COMPUTERS\Desktop\meet up wk3\data.txt"
# with open(our_file, mode = "r") as file:
#          content = file.read()
#          print(content)

# 4

# def count_lines():
#         with open("data.txt", mode = "r") as file:
#             lines = file.readlines()
#             return len(lines)
#         print(lines)
# print(f"the number of count is:", count_lines()) 
 
# 5
# file_name = r"C:\Users\C PLUG COMPUTERS\Desktop\meet up wk3\data.txt"
# def read_file():
#          try:
#                 with open("file_name", mode = "r") as file:
#                     content = file.read()
#                     print(content)
#          except FileNotFoundError:
#                     print("File not found!")
# print(read_file())

# 6

# def word_count():
#     try:
#         with open("data.txt", mode = "r") as file:
#             content = file.read()
#             words = content.split()
#             print("Word count:", len(words))
#     except FileNotFoundError:
#         print("File not found.")
# #     except Exception as error:
#         # print("An error occured:", str(error))

# print(word_count())


