a=input("enter a word: ")
alpha={}
for i in a:
    alpha[i]=alpha.get(i,0)+1
print(alpha)
