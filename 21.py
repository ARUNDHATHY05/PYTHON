a=input("enter a sentence")
words={}
print("frequency of words: ")
for i in a.split():
    words[i]=words.get(i,0)+1
print(words)

