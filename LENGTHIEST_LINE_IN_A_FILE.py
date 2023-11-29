import os
op=open("open.txt","r")
ls=op.readlines()
ls.sort(key=len,reverse=True)
length=len(ls[0]);
print("Length of longest line is ",length,"\n The lines are:")
[print(x) for x in ls if len(x)==length]
op.close()
