import os
op=open("openfile.txt","r")
ls=op.readlines()
print("The number of lines in the files is ",len(ls))
op.close()
