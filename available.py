n=input("enter a list of items seperated by comma: ")
n=n.split(',')
item=input("enter an item to check: ")
if item in n:
    result='available'
else:
        result='not available'
print("the item",item,"is",result,"in the list.")
