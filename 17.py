s=['ab','cd',12,12,'cd',13]
new=[]
print("after removing")
for i in s:
   if(i not in new):
      new.append(i)
      print(i)
   
