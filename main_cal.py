import func_cal

cal_counter = 0
result_list = []

print ("calculator")
while True:
    print("1=덧셈 2=뺄셈 3=곱셈 4=나눗셈 5=결과창 6=결과창 reset")
    cal_type = int(input())

    if cal_type < 5:

        cal_counter = cal_counter + 1

        print("첫번째 숫자를 입력하시오")
        firstnum = int(input())
        print("두번째 숫자를 입력하시오")
        secondnum = int(input())
            
        if cal_type == 1:
            result = func_cal.add_func(firstnum,secondnum)
        elif cal_type ==2:
            result = func_cal.minus_func(firstnum,secondnum)
        elif cal_type == 3:
            result = func_cal.supple_func(firstnum,secondnum)
        elif cal_type ==4:
            result = func_cal.seperate_func(firstnum,secondnum)
        else:
            result = ("none")

        print(result)
        #result_list[] = result_list + result
        result_list.append(result)

    if cal_type ==5:
        print(result_list)

    if cal_type ==6:
        cal_counter = 0
        result_list = list()