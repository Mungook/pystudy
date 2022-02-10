import cal_func

print("계산기 모드를 선택하십시오: ")
print("1: 더하기, 2: 빼기, 3: 곱하기, 4: 나누기")
cal_mode = int(input())

print("계산할 첫번째 숫자를 입력하십시오: ")
input_a = int(input())
print("계산할 두번째 숫자를 입력하십시오: ")
input_b = int(input())

if(cal_mode==1):
    print("{} + {} = {}".format(input_a, input_b, cal_func.add_num(input_a, input_b)))

elif(cal_mode==2):
    print("{} - {} = {}".format(input_a, input_b, cal_func.sub_num(input_a, input_b)))

elif(cal_mode==3):
    print("{} * {} = {}".format(input_a, input_b, cal_func.mul_num(input_a, input_b)))

elif(cal_mode==4):
    print("{} / {} = {}".format(input_a, input_b, cal_func.div_num(input_a, input_b)))

else:
    print("error...")