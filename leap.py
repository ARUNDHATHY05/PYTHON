year=int(input("enter an upcoming year"))
print("leap year from 2023 to",year,"are: ")
for i in range(2023,year+1):
    if((i%4==0) and (i%100!=0) or (1%400==0)):
        print(i)
