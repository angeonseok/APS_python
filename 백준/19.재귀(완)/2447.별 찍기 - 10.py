"""
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

#입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

#출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
"""

import sys
input = sys.stdin.readline

n = int(input())

#공백만들기
arr = [[" "] * n for _ in range(n)]

#분할정복
def star(arr, r, c, n):

    #더 못쪼개면 별찍어
    if n == 1:
        arr[r][c] = "*"
        return
    
    #전체를 9등분하겠다
    n = n // 3
    for i in range(3):
        for j in range(3):

            #9등분 기준 중앙은 공백으로 둬야지
            if i == 1 and j == 1:
                continue
            else:
                star(arr, r + i*n, c+ j*n, n)

star(arr, 0, 0, n)
for row in arr:
    print("".join(row))