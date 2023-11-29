import os
op=open("openfile.txt","r")
oddneven=op.readlines()
oddneven.pop()
ls=[x[0:-1] for x in oddneven]
print (ls)
even=[x for x in ls if not int(x)%2]
odd=[x for x in ls if int(x)%2]
op.close()
op2=open("even.txt","w")
evenfinal=[x+"\n" for x in even]
op2.writelines(evenfinal)
op2.close()
op3=open("odd.txt","w")
oddfinal=[x+"\n" for x in odd]
op3.writelines(oddfinal)
op3.close()
