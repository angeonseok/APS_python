# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

#입력
#첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

#출력
#첫째 줄에 N!을 출력한다.

a = int(input())

def fac(i):
    if i == 0:
        return 1
    else :
        return i * fac(i-1)

b = fac(a)
print(int(b))
        
        

