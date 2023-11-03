def sum(seq):
    if len(seq)==1:
        return seq[0]
    else:
        return seq[0]+sum(seq[1:])
l=input("enter list: ")
l=l.split()
l=[int (x) for x in l]
print("sum: ",sum(l))
