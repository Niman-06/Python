#question 1

# month = int(input("Enter month number (1-12): "))

# if month == 1:
#     print("January")
# elif month == 2:
#     print("February")
# elif month == 3:
#     print("March")
# elif month == 4:
#     print("April")
# elif month == 5:
#     print("May")
# elif month == 6:
#     print("June")
# elif month == 7:
#     print("July")
# elif month == 8:
#     print("August")
# elif month == 9:
#     print("September")
# elif month == 10:
#     print("October")
# elif month == 11:
#     print("November")
# elif month == 12:
#     print("December")
# else:
#     print("Invalid month number")

#question 2

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Equal" if a == b else "Not Equal")
# print("First is Bigger" if a > b else "Second is Bigger" if b > a else "Both Equal")
# print("First is Smaller or Equal to Second" if a <= b else "First is Greater")

# if a > b:
#     for i in range(5):
#         print("Niman")
# elif a < b:
#     for i in range(3):
#         print("Preetkaur")

#question 3

# a = input("Enter first string: ")
# b = input("Enter second string: ")

# print("Equal" if a == b else "Not Equal")
# print("Equal" if a is b else "Not Equal")
 
#question 4

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# n1 = int(s1)
# n2 = int(s2)

# if n1 is n2:
#     print("Both numbers are equal")
# else:
#     print("Both numbers are not equal")

#question 5

# n = int(input("Enter a number: "))
# print("Sum =", n * (n + 1) // 2)

#question 6

# n = int(input("Enter a number: "))

# for i in range(2, n + 1, 2):
#     print(i, end=",")

#question 7

# name = input("Enter Name: ")
# age = int(input("Enter Age: "))

# print("1. First Class - 1500")
# print("2. Second Class - 1000")
# print("3. Sleeper Class - 500")

# c = int(input("Choose Class (1-3): "))

# if c == 1:
#     price = 1500
#     cls = "First Class"
# elif c == 2:
#     price = 1000
#     cls = "Second Class"
# else:
#     price = 500
#     cls = "Sleeper Class"

# if age < 5:
#     price = 0
# elif age >= 60:
#     price = price - (price * 20 / 100)

# meal = input("Meal Required (yes/no): ")

# if meal.lower() == "yes":
#     price += 200

# print("\n--- Ticket Details ---")
# print("Name:", name)
# print("Age:", age)
# print("Class:", cls)
# print("Final Ticket Price: ₹", price) 

# question 8

# print("Welcome to Burger King 🍔")

# print("1. Whopper Burger - ₹150")
# print("2. Crispy Veg - ₹100")
# print("3. Chicken Wings - ₹120")

# item = int(input("Choose item (1-3): "))
# qty = int(input("Enter quantity: "))

# if item == 1:
#     price = 150
#     name = "Whopper Burger"
# elif item == 2:
#     price = 100
#     name = "Crispy Veg"
# else:
#     price = 120
#     name = "Chicken Wings"

# total = price * qty

# coupon = input("Enter coupon code: ")

# if coupon == "KING50":
#     total = total * 0.5
# elif coupon == "BK20":
#     total = total - 20

# print("\n----- BILL -----")
# print("Item:", name)
# print("Quantity:", qty)
# print("Final Bill: ₹", total)

