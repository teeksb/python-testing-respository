# COntinue statment is for skipping iterations.
# It skips only the current iteration and move sto the next.


for num in range (1, 11):
    if num % 2 == 0:
         print("What are the numbers being skipped", num)
         continue
    
    print(num)