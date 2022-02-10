import studycal
from math import *
print('숫자를 입력하세요')


num_1=input()

if num_1 == float:
   a=[num_1]
else: 
   print('계산할 수식형을 선정하세요 ')
   print('1. sin 2. cos 3. tan 4. log')
   mode = int(input())
   if mode == 1:
      print('sin함수를 선택하였습니다 sin(x)의  x 값을 대입하세요') 
      num_1 = sin(float(input()))
      a=[num_1]
      print(num_1)
   elif mode == 2:
       print('cos함수를 선택하였습니다 cos(x)의  x 값을 대입하세요') 
       num_1 = cos(float(input()))
       a=[num_1]
       print(num_1)
   elif mode == 3: 
       print('tan함수를 선택하였습니다 tan(x)의  x 값을 대입하세요') 
       num_1 = tan(float(input()))
       a=[num_1]
       print(num_1)
   elif mode == 4:
       print('log 함수를 선택하셨습니다. 밑수와 진수를 차례로 입력하세요')
       a = int(input())
       n_1 = int(input())
       num_1 = log(n_1 , a)
       a=[num_1]
       print(num_1) 
       print('로그값')
   else :
       print('Error...')

unit_1= str(input())
    

#insert 를 이용해보자
#덧셈
if unit_1== '+' : 
    num_2=input()
    if num_2 == float:
     alist=[num_1]   
     alist.insert(1,num_2)
    else: 
     print('계산할 수식형을 선정하세요 ')
     print('1. sin 2. cos 3. tan 4. log')
     mode = int(input())
     alist=[num_1] 
     if mode == 1:
      print('sin함수를 선택하였습니다 sin(x)의  x 값을 대입하세요') 
      num_2 = sin(float(input()))
      alist.insert(1,num_2)
      print(num_1, unit_1, num_2)
     elif mode == 2:
       print('cos함수를 선택하였습니다 cos(x)의  x 값을 대입하세요') 
       num_2 = cos(float(input()))
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
       
     elif mode == 3: 
       print('tan함수를 선택하였습니다 tan(x)의  x 값을 대입하세요') 
       num_2 = tan(float(input()))
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
     elif mode == 4:
       print('log 함수를 선택하셨습니다. 밑수와 진수를 차례로 입력하세요')
       a = int(input())
       n_1 = int(input())
       num_2 = log(n_1 , a)
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
     else :
       print('Error...')



    
    unit_2 =str(input())
    if unit_2 == '=':
      print(alist[0]+alist[1])
    else:
      num_3 = float(input())

# 뺄셈

elif unit_1== '-' : 
    num_2=input()
    if num_2 == float:
     alist=[num_1]   
     alist.insert(1,num_2)
    else: 
     print('계산할 수식형을 선정하세요 ')
     print('1. sin 2. cos 3. tan 4. log')
     mode = int(input())
     alist=[num_1] 
     if mode == 1:
      print('sin함수를 선택하였습니다 sin(x)의  x 값을 대입하세요') 
      num_2 = sin(float(input()))
      alist.insert(1,num_2)
      print(num_1, unit_1, num_2)
     elif mode == 2:
       print('cos함수를 선택하였습니다 cos(x)의  x 값을 대입하세요') 
       num_2 = cos(float(input()))
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
       
     elif mode == 3: 
       print('tan함수를 선택하였습니다 tan(x)의  x 값을 대입하세요') 
       num_2 = tan(float(input()))
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
     elif mode == 4:
       print('log 함수를 선택하셨습니다. 밑수와 진수를 차례로 입력하세요')
       a = int(input())
       n_1 = int(input())
       num_2 = log(n_1 , a)
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
     else :
       print('Error...')



    
    unit_2 =str(input())
    if unit_2 == '=':
      print(alist[0]-alist[1])
    else:
      num_3 = float(input())
#곱셈      

elif unit_1== '*' : 
    num_2=input()
    if num_2 == float:
     alist=[num_1]   
     alist.insert(1,num_2)
    else: 
     print('계산할 수식형을 선정하세요 ')
     print('1. sin 2. cos 3. tan 4. log')
     mode = int(input())
     alist=[num_1] 
     if mode == 1:
      print('sin함수를 선택하였습니다 sin(x)의  x 값을 대입하세요') 
      num_2 = sin(float(input()))
      alist.insert(1,num_2)
      print(num_1, unit_1, num_2)
     elif mode == 2:
       print('cos함수를 선택하였습니다 cos(x)의  x 값을 대입하세요') 
       num_2 = cos(float(input()))
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
       
     elif mode == 3: 
       print('tan함수를 선택하였습니다 tan(x)의  x 값을 대입하세요') 
       num_2 = tan(float(input()))
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
     elif mode == 4:
       print('log 함수를 선택하셨습니다. 밑수와 진수를 차례로 입력하세요')
       a = int(input())
       n_1 = int(input())
       num_2 = log(n_1 , a)
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
     else :
       print('Error...')



    
    unit_2 =str(input())
    if unit_2 == '=':
      print(alist[0]*alist[1])
    else:
      num_3 = float(input())
#나눗셈      

elif unit_1== '/' : 
    num_2=input()
    if num_2 == float:
     alist=[num_1]   
     alist.insert(1,num_2)
    else: 
     print('계산할 수식형을 선정하세요 ')
     print('1. sin 2. cos 3. tan 4. log')
     mode = int(input())
     alist=[num_1] 
     if mode == 1:
      print('sin함수를 선택하였습니다 sin(x)의  x 값을 대입하세요') 
      num_2 = sin(float(input()))
      alist.insert(1,num_2)
      print(num_1, unit_1, num_2)
     elif mode == 2:
       print('cos함수를 선택하였습니다 cos(x)의  x 값을 대입하세요') 
       num_2 = cos(float(input()))
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
       
     elif mode == 3: 
       print('tan함수를 선택하였습니다 tan(x)의  x 값을 대입하세요') 
       num_2 = tan(float(input()))
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
     elif mode == 4:
       print('log 함수를 선택하셨습니다. 밑수와 진수를 차례로 입력하세요')
       a = int(input())
       n_1 = int(input())
       num_2 = log(n_1 , a)
       alist.insert(1,num_2)
       print(num_1, unit_1, num_2)
     else :
       print('Error...')



    
    unit_2 =str(input())
    if unit_2 == '=':
      print(alist[0]/alist[1])
    else:
      num_3 = float(input())













elif unit_1== '=':
    print(num_1)
else:    
    print('Error...')








    




