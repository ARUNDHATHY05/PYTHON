s=input("enter a sentence: ")
s=s.split()
s=[]
for i in s:
    if len(i)==len(max(s,key=len)):
        print("longest word: ",len(i))
        if len(s)>1:
            print("BINGO")

