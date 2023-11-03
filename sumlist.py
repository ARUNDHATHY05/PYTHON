def sum_list(l):
    sum=0
    for i in l:
        sum+=i
        return sum
n=input("enter comma seperated elements: ")
n=list(map(int,n.split(' ')))
print("sum of elements: ",sum_list(n))
