percentage=float(input("enter the percentage of marks: "))
if 90<=percentage<100:
    grade="A+"
elif 80<=percentage<90:
    grade="B+"
elif 70<=percentage<80:
    grade="B"
elif 60<=percentage<70:
    grade="C+"
elif 50<=percentage<60:
    grade="C"
elif 40<=percentage<50:
    grade="D+"
elif 30<=percentage<40:
    grade="D"
else:
   grade="E(FAILED!!!)"
print("the grade for",percentage,"is: ",grade)
            
       
