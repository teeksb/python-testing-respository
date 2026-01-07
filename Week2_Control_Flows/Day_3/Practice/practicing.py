# # colors = ["red", "yellow", "green"]

# # for color in colors:
# #     print(color)

# # for i in range(5):
# #     print(i)


# # print ("")
# # print ("")

# # light = ""

# # while light not in ("red", "yellow", "green"):
# #     light = input("Enter a valid traffic light color: ").lower()

# # print("You entered:", light)


# # count = ""

# # while count < 3:
# #     print(count)
#     count += 1



# while True:
#     age = int(input("Enter your age: "))

#     if age >= 18:
#         print("Access granted")
#         break
#     else:
#         print("Try again")

# # password = "story"
# # while password != "secret":
# #     password = input("Try again: ")
# # else:
# #     print("COrrect)")

# print (***************************)
# Check if user is over 18 and warn if not (if)
# # age = 20

# # if age >= 18:
# #     print("Adult")

# attempts = 0

# while attempts < 3:
#     password = input("Password: ")
#     attempts += 1
# age = int(input("What is your age? "))

# while age < 18:
#     print("Warning: You must be 18+.")
#     age = int(input("What is your age? "))

# print("Access allowed.")

# print (***************************)
# Keep asking for a valid email until it is valid (while)
# email = ""

# while "@" not in email or "." not in email:
#     email = input("Enter a valid email: ")

# print("Email accepted:", email)

# print (***************************)
# # Run some code exactly 10 times (for)
# for i in range(10):
#     print("Running task", i + 1)

# print (***************************)
# Process each transaction and flag suspicious ones (for + if)
# transactions = [50, 1200, 20, 5000, 75]
# threshold = 1000

# for amount in transactions:
#     if amount > threshold:
#         print("Suspicious transaction:", amount)

# print (***************************)
# Retry an API request until success or 5 attempts (while)
# attempts = 0
# success = False

# while attempts < 5 and not success:
#     attempts += 1
#     print(f"Attempt {attempts}...")

#     # Simulated API result (replace with real call)
#     response_ok = (attempts == 3)

#     if response_ok:
#         success = True
#         print("Request succeeded!")
#     else:
#         print("Request failed. Retrying...")

# if not success:
#     print("Failed after 5 attempts.")

# Check config value exists, else use default (if)
# config_timeout = None  # could be None if not set
# default_timeout = 30

# print (***************************)
# if config_timeout is None:
#     timeout = default_timeout
# else:
#     timeout = config_timeout

# print("Timeout:", timeout)

# print (***************************)
# Loop through password chars and count digits (for)
# password = "aB3d9X1"
# digit_count = 0

# for ch in password:
#     if ch.isdigit():
#         digit_count += 1

# print("Digits:", digit_count)


# print (***************************)
# Show a menu until user chooses Exit (while)
# choice = ""

# while choice != "3":
#     print("\nMenu")
#     print("1. View profile")
#     print("2. Settings")
#     print("3. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         print("Profile page...")
#     elif choice == "2":
#         print("Settings page...")
#     elif choice == "3":
#         print("Goodbye!")
#     else:
#         print("Invalid choice. Try again.")

# print (***************************)
# Apply a discount once if user is premium (if)
is_premium = True
total = 100

if is_premium:
    total = total * 0.9  # 10% discount

print("Final total:", total)