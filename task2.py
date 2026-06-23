# question1
# string = input("Enter a string: ")

# if len(string) < 2:
#     print("not a valid string")
# else:
#     result = string[:2] + string[-2:]
#     print(result)

# question2
# a = input("Enter first string: ")
# b = input("Enter second string: ")

# print(b[0] + a[1:], a[0] + b[1:])

# question3
# s = input("Enter a string: ")
# if len(s) < 3:
#     print(s)
# elif s.endswith("ing"):
#     print(s + "ly")
# else:
#     print(s + "ing")

# list ques 1
# friends = ["Aman", "Ravi", "Simran", "Karan", "Priya"]

# name = input("Enter another friend: ")
# friends.append(name)

# print(friends)

# important = input("Most important friend: ")
# pos = int(input("Enter position: "))

# friends.insert(pos, important)

# print(friends)

# ques2
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(numbers)

# ques3
# a = [1, 10, 100, 3, 6, 8]
# a.insert(3, 59)
# a.append(5)
# print(a)
# print(len(a))

# ques4
# words = ["pen", "book", "car", "school", "bus", "tree"]
# for i in words:
#     if len(i) < 4:
#         print(i)

# ques5
# numbers = range(20)
# result = []
# for i in numbers:
#     if i % 2 == 0:
#         result.append("even")
#     else:
#         result.append("odd")

# print(result)

# ques6
# for i in range(1, 1001):
#     if i % 7 == 0:
#         print(i)

# ques7
# s = input("Enter a string: ")
# print(s.count(" "))

# ques8
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
# for i in list_a:
#     if i in list_b:
#         print(i)