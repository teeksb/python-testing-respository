# Continue stateent helps you to skip an iteration and can be based ona given condition or criteria
# A break you break out of the loop entriely
# They are also referred to as loop controls because the y help in the 
# Break stateement is often used with if statement.

# found = False

# for num in range(1, 1000):
#     guess = int(input("Guess the number: "))
#     if guess == 42:
#         found = True
#         print("Correct! You've found the number 42!")
    
#     if not found:
#         print("Try again!")



for num in range(1, 1000):
    guess = int(input("Guess the number: "))
    if guess == 42:
        print("Correct! You've found the number 42!")
        break #This ends/exits the parent loop

    print("Try again!")


for num in range (1, 1001):
  if num > 20:
     break
  
  if num % 2 == 0:
     print (num)