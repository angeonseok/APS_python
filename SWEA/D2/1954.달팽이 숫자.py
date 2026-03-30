# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

#제약사항
# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

#입력
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.

#출력
# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

import sys
input = sys.stdin.readline

T = int(input())

#하, 우, 상, 좌 순으로 델타 정렬
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]          

for a in range(1,T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    x = 0
    y = 0
    d = 0
    cnt = 1

    #배열 만들었으면 안에서 작업해야지
    for _ in range(n * n):
        
        #탐색한 칸을 칠해
        arr[x][y] = cnt

        #다음 좌표
        nx = x + dx[d]
        ny = y + dy[d]

        #다음 좌표가 불가능한가? 왔던 길 또 가는 건가?
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x = nx
            y = ny
        
        #그렇다면 d값 변환시켜서 다시 도전
        else:
            d = (d + 1) % 4
            x = x + dx[d]
            y = y + dy[d]

        #이동하면 카운트 늘려
        cnt += 1
    
    print(f'#{a}')
    for i in arr:
        print(*i)