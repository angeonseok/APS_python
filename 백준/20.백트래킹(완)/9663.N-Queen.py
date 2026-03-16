"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

#출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
"""

import sys
input = sys.stdin.readline

#일단 놨을 때, 이전 배치들과 충돌나는지 체크
def check(col):
    for i in range(col):
        #대각선 위치면 컷(행 차이 == 열 차이)
        #같은 열이면 컷
        if abs(maps[i] - maps[col]) == abs(col - i) or maps[i] == maps[col]:
            return False

    return True

def N_queen(row):
    global cnt

    if row == n:    #가능한 경우에 카운팅
        cnt += 1
        return
    
    for i in range(n):      #모든 열에 대해서 조사
        maps[row] = i       #먼저 놓고
        if check(row):      #가능한 위치면
            N_queen(row+1)  #다음 행으로 진행

n = int(input())
maps = [0] * n      #인덱스 = 행, 데이터 값 = 열
cnt = 0

N_queen(0)
print(cnt)