num=input("enter the numbers seperated by comma: ")
numlist=num.split()
small=int(numlist[0])
large=int(numlist[0])
for i in numlist:
    if(int(i)>large):
        large=int(i)
        elif int(i)<small:
            small=int(i)
            print("list is: ",numlist)
            print("THE LARGEST ELEMENT IS: ",large)
            print("THE SMALLEST ELEMENT IS: ",small)
