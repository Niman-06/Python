# def input_something(msg):
#     while True:
#         x = input(msg).strip()
#         if x:
#             return x
#         print("Input cannot be blank.")
# def input_int(msg):
#     while True:
#         try:
#             return int(input(msg))
#         except ValueError:
#             print("Enter a valid integer.")

# movies = [
#     {"name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"]},
#     {"name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action", "Adventure", "Drama"]},
#     {"name": "Back to the Future", "year": 1985, "duration": 114, "genres": ["Adventure", "Comedy", "Sci-Fi"]}
# ]

# print("Welcome to Movie Database!")

# while True:
#     choice = input("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit: ").lower()

#     if choice == "a":
#         genres = []
#         while not genres:
#             genres = [g.strip() for g in input_something("Genres (comma separated): ").split(",") if g.strip()]

#         movies.append({
#             "name": input_something("Name: "),
#             "year": input_int("Year: "),
#             "duration": input_int("Duration: "),
#             "genres": genres
#         })
#         print("Movie added.")

#     elif choice == "l":
#         if not movies:
#             print("No movies saved.")
#         else:
#             for i, m in enumerate(movies, 1):
#                 print(f"{i}) {m['name']} ({m['year']})")

#     elif choice == "s":
#         if not movies:
#             print("No movies saved.")
#         else:
#             condition = input_something("Search: ").lower()
#             for i, m in enumerate(movies, 1):
#                 if condition in m["name"].lower():
#                     print(f"{i}) {m['name']} ({m['year']})")

#     elif choice == "v":
#         if not movies:
#             print("No movies saved.")
#         else:
#             i = input_int("Index: ") - 1
#             if 0 <= i < len(movies):
#                 m = movies[i]
#                 print(f"Name: {m['name']}")
#                 print(f"Year: {m['year']}")
#                 print(f"Duration: {m['duration']} mins")
#                 print("Genres:", ", ".join(m["genres"]))
#             else:
#                 print("Invalid index number.")

#     elif choice == "d":
#         if not movies:
#             print("No movies saved.")
#         else:
#             i = input_int("Index: ") - 1
#             if 0 <= i < len(movies):
#                 print(f"{movies.pop(i)['name']} deleted.")
#             else:
#                 print("Invalid index number.")

#     elif choice == "q":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice.")