# question1
# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# ques2
# for num in range(2, 101):
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print(num)


# ques3
# score = int(input("Enter score: "))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# ques4
# n = int(input("Enter number: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)

# ques5
# squares = [i**2 for i in range(1, 21) if i % 2 == 0]
# print(squares)

# ques6
# year = int(input("Enter year: "))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")

# ques7
# a = int(input("Side 1: "))
# b = int(input("Side 2: "))
# c = int(input("Side 3: "))
# if a == b == c:
#     print("Equilateral")
# elif a == b or b == c or a == c:
#     print("Isosceles")
# elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
#     print("Right Angle Triangle")
# else:
#     print("Scalene")

# ques8
# n = int(input("Enter number: "))
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")

# ques9
# weight = float(input("Enter weight (kg): "))
# height = float(input("Enter height (m): "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal Weight")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obesity")

# ques10
# day = int(input("Enter day number: "))
# days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# if 1 <= day <= 7:
#     print(days[day-1])
# else:
#     print("Invalid Day")

# ques11
# price = float(input("Enter price: "))
# if price > 1000:
#     discount = price * 0.10
# elif price >= 500:
#     discount = price * 0.05
# else:
#     discount = 0

# print("Discount =", discount)
# print("Final Price =", price - discount)

# ques12
# n = int(input("Enter n: "))
# print("Sum =", n * (n + 1) // 2)

# ques13
# employee_details = {
#     1: {"name": "Aman", "salary": 60000},
#     2: {"name": "Raman", "salary": 45000},
#     3: {"name": "Simran", "salary": 70000}
# }
# result = [emp["name"] for emp in employee_details.values()
#           if emp["salary"] > 50000]
# print(result)

# ques14
# s = input("Enter string: ")
# count = 0
# for ch in s.lower():
#     if ch in "aeiou":
#         count += 1
# print("Vowels =", count)

# ques15
# num = input("Enter number: ")
# total = 0
# for i in num:
#     total += int(i)
# print("Sum =", total)

# ques16
# n = 5
# for i in range(1, n + 1):
#     print("*" * i)

# ques17
# import random
# num = random.randint(1, 100)
# while True:
#     guess = int(input("Guess: "))
#     if guess > num:
#         print("Too High")
#     elif guess < num:
#         print("Too Low")
#     else:
#         print("Correct!")
#         break

# ques18
# n = int(input("Enter number: "))
# for i in range(2, n + 1, 2):
#     print(i, end=" ")

# ques19
# lst = [10, 25, 30, 25, 40, 50, 60, 70, 80, 90]
# print("25 Exists:", 25 in lst)
# print("Length:", len(lst))
# print("Occurrence of 25:", lst.count(25))
# for i in lst:
#     print(i)
# print("Even Numbers:")
# for i in lst:
#     if i % 2 == 0:
#         print(i)

# ques20
# s = input("Enter string (10-19 words): ")
# words = s.split()
# print("String:", s)
# print("Length:", len(s))

# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
# print("Middle Word:", words[len(words)//2])
# print("Second Last Word:", words[-2])

# ques21
# print("Welcome to Calci")
# print("1. Power")
# print("2. Sum")
# print("3. Sub")
# print("4. Multiple")

# choice = int(input("Enter choice: "))
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if choice == 1:
#     print("Power =", a ** b)
# elif choice == 2:
#     print("Sum =", a + b)
# elif choice == 3:
#     print("Sub =", a - b)
# elif choice == 4:
#     print("Multiple =", a * b)
# else:
#     print("Invalid Choice")

# ques22
# x = ['abc', 'xyz', 'aba', '1221']

# count = 0
# for i in x:
#     if len(i) >= 2 and i[0] == i[-1]:
#         count += 1
# print(count)