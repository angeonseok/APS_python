"""
N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.

#입력
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.
다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다. 각 문자는 'o'또는 '.'으로, 'o'는 돌이 있는 칸을 의미하고, '.'는 돌이 없는 칸을 의미한다.

#출력
각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다.
"""

T =int(input())
for tc in range(1, T+1):
    n = int(input())
    m = [input().strip() for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            #돌이 있는 부분부터 탐색
            if m[i][j] == 'o':
                for dir in [(-1,1), (0,1),(1,1),(1,0)]:
                    cnt = 0
                    ni, nj = i, j

                    #방향 유지하면서 5개 이상 체크될 때 까지 확인
                    while 0 <= ni < n and 0 <= nj < n and m[ni][nj] =='o':
                        cnt += 1
                        ni += dir[0]
                        nj += dir[1]

                    #체크 되면 다 빠져나가
                    if cnt >= 5:
                        ans = 1
                        break
                if ans:
                    break
        if ans:
            break       
   
    if ans:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')