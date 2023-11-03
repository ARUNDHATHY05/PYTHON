def sum_list(input_list):
    total=0
    for num in input_list:
        total+=num
        return total
user_input=input("enter a list of numbers seperated by comma: ")
user_num=[int(x) for x in user_input.split()]
if user_num:
    result=sum_list(user_num)
    print("sum of elements: ",result)


