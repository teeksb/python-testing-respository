# A while loop is a loop that runs based on a condition. The loop does not nend until as set condition resolves to false else it runs
# for infinity.

# One of the common ways to stop a while loop is the use of a flag.

#Basic syntax
# while condition:
#     do_something

# When to use while :
# Unkown number of repeats
# User input/retries
# Waiting for a condition
# Game loops
# Polling /retry logic

count = 1 #the flag
while count <= 5:            #loop condition that must be true or false - it eeps running until it is false
    print(count)             #repeated action of the loop
    count = count + 1       # this is what updates the flag - this helps the loop know whento stop , otherwise the loop will go on and on.

print ("I'm outside the while loop")

count = 1 
while count <= 5:           
    print(count)            
    count = count + 1       
print ("I'm outside the while loop")