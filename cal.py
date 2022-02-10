import math
sum1 = []
while True :
    print("연산을 선택하시오")
    print("(1=덧셈, 2=뺄셈, 3=곱셈, 4=나눗셈, 5=삼각함수 6=나가기)")
    num1 = int(input())
    print("계산값 = %s"%sum1)
    if num1 < 5 :
        print("첫번째 숫자를 입력하세요 : ")
        num2 = int(input())
        print("두번째 숫자를 입력하세요 :")
        num3 = int(input())
        if num1 == 1 :
            num4 = num2 + num3
            print("%d + %d = %d" %(num2,num3,num4))
        elif num1 == 2 :
            num4 = num2 - num3
            print("%d - %d = %d" %(num2,num3,num4))
        elif num1 == 3 :

            num4 = num2 * num3
            print("%d * %d = %d" %(num2,num3,num4))
        elif num1 == 4 :
            num4 = num2 / num3
            print("%d / %d = %d" %(num2,num3,num4))
    elif num1 == 5 :
        print("sin, cos, tan 중 하나를 선택하시오")
        print("1 = sin, 2 = cos, 3 = tan")
        num5 = int(input())
        print("각도를 입력하시오.")
        num6 = int(input())
        if num5 == 1 :
            num4 = math.sin(math.pi*(num6/180))
            print("sin(%d) = %d"%(num6,num4))
        if num5 == 2 :
            num4 = math.cos(math.pi*(num6/180))
            print("cos(%d) = %.2f"%(num6,num4))
        if num5 == 3 :
            num4 = math.tan(math.pi*(num6/180))
            print("tan(%d) = %d"%(num6,num4))

    elif num1 == 6 :
        break
    sum1.append(num4)