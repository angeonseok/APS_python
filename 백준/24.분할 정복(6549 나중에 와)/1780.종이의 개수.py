"""
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.
1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
2 .(1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

#입력
첫째 줄에 N(1 ≤ N ≤ 3^7, N은 3^k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

#출력
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
"""

import sys
input = sys.stdin.readline

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]
a, b, c, = 0, 0, 0

def cut_9(x,y,n):
    global a, b, c

    first = p[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if p[i][j] != first:

                c_nine = n // 3

                #나눌때 가로 > 세로 순으로 잘 하자
                for dx in range(3):
                    for dy in range(3):
                        cut_9(x + dx*c_nine, y + dy*c_nine, c_nine)
                return
            
    if first == -1:
        a += 1
    elif first == 0:
        b += 1
    else:
        c += 1

cut_9(0,0,n)
print(a, b, c,sep='\n')