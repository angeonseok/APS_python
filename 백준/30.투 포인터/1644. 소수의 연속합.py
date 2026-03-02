"""
하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.
3 : 3 (한 가지)
41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
53 : 5+7+11+13+17 = 53 (두 가지)
하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.
자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)

#출력
첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.
"""

import sys
input = sys.stdin.readline

n = int(input())

#소수생성
def prime(n):
    p = [True] * (n + 1)
    p[0] = False
    p[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if p[i] : 
            for j in range(i * i, n + 1, i):
                p[j] = False
    
    return p

#대응되는 수로 전환
arr = prime(n)
prime_list = []
for i in range(len(arr)):
    if arr[i]:
        prime_list.append(i)

l, r = 0, 0
sum_num = 0
cnt = 0

while r < len(prime_list):

    #부분합을 이용
    sum_num += prime_list[r]
    r += 1

    while sum_num > n :
        sum_num -= prime_list[l]
        l += 1

    #소수합이 주어진 수와 같으면 카운팅
    if sum_num == n:
        cnt += 1

print(cnt)