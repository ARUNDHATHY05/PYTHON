a=input("enter collection 1: ")
a=set(map(int,a.split(',')))
c=input("enter collection 2: ")
c=set(map(int,c.split(',')))
len(a)==len(c)
print("list are of same length: ",len(a)==len(c))