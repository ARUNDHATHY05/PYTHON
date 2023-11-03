def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
user_input=int(input("enter a number:"))
if user_input>=0:
    result=factorial(user_input)
    print("factorial of",user_input,"is",result)
else:
    print("invalid choice")
