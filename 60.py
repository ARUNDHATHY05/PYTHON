import os
op=open("open.txt","r")
ls=op.read().split()
ls.sort(key=len,reverse=True)
length=len(ls[0]);
print("LENGTH OF THE WORD: ",length,"\nWORD: ");
[print(x) for x in ls if len(x)==length]
op.close()
