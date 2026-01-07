#List SLicing - is to get a chunk/part of a list

names = ["Mike", "Jane", "Blessing", "Peter", "Joe", "Sarah", "Chris", "Daniel", "Jasper", "Irine"]

#Get names from the 3rd to 6th position in the list.
#The end position should always be =1 where we intend to end/stop
print(names[2:6])

print(names[:]) #Gives all items in the list
print(names[: 4]) #Gives all items from start of list to he 3rd index position - end is -1
print(names[2: ]) #Gives all items from 3rd index of list to the lastposition - forwad is =+1
