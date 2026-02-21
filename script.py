
# name = "JR"
# age = 45
# location = "Chattanooga"
# fav_snack = "Granola"
# Super_Bowl = "Seahawks"

# print("My name is", name)
#
# name = input("What is your name?")
# age = input("How old are you?")
# location = input("Where do you live?")
#
# print(f"Hello {name}, you are {age} years old and you are from {location}")
# ---------------------------
# This program automatically calculates the spending budget for Frank.

pay = 1200 # This is an integer
pay_raise = .10 # This is a float
name = "Frank" # This is a string
expenses = [.10, 5.20, 7.30] # This is a list

remaining = pay-100 # This is an operation
print("The remaining balance is" ,remaining, "dollars")

# remaining = pay-100
# print(f"The remaining balance is ${remaining}")
# print(f"The remaining balance is ${pay-100}")

pay = pay-200 # This is an update to the original variable that was defined in line 18

# print("The pay is now", pay)
print(f"The pay is now ${pay-200}")

remaining = pay-expenses[0]
print("The remaining balance is", remaining, "dollars")


