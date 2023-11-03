a,b=0,1
for i in range(n):
    a,b=b,a+b
    return a
n=int(input("enter number"))
print("%d fibanocci number is %d"%(n,fibo(n)))
if m==0:
    return 0
if n==1:
    return 1
else:
    return fibo(n-1)+fibo(n-2)
