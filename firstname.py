firstname=input("enter the names seperated by comma")
count=0
for name in firstname:
    if name.startswith('A'):
     count=count+1
print("number of names are: ",count)
