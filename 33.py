def even(l):
    for i in l:
        if(i==237):
            break
        elif not i%2:
            print(i)
n=input("enter the input")
n=list(map(int,n.split()))
even(n)
