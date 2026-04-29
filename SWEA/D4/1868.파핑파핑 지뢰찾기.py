"""
'파핑 파핑 지뢰 찾기'라는 유명한 게임이 있다. 이 게임은 RXC 크기의 표를 이용하는 게임인데,
표의 각 칸에는 지뢰가 있을 수도 있고 없을 수도 있다.
표의 각 칸을 클릭했을 때, 그 칸이 지뢰가 있는 칸이라면 '파핑 파핑!'이라는 소리와 함께 게임은 끝난다.
지뢰가 없는 칸이라면 변이 맞닿아 있거나 꼭지점이 맞닿아 있는 최대 8칸에 대해 몇 개의 지뢰가 있는지가 0에서 8사이의 숫자로 클릭한 칸에 표시된다.
만약 이 숫자가 0이라면 근처의 8방향에 지뢰가 없다는 것이 확정된 것이기 때문에 그 8방향의 칸도 자동으로 숫자를 표시해 준다.
실제 게임에서는 어떤 위치에 지뢰가 있는지 알 수 없지만, 이 문제에서는 특별히 알 수 있다고 하자.
지뢰를 '*'로, 지뢰가 없는 칸을 '.'로, 클릭한 지뢰가 없는 칸을 'c'로 나타냈을 때 표가 어떻게 변화되는지 나타낸다.
세 번째 예에서는 0으로 표시 될 칸들과 이와 인접한 칸들이 한 번의 클릭에 연쇄적으로 숫자가 표시된 것을 볼 수 있다.
파핑 파핑 지뢰 찾기를 할 때 표의 크기와 표가 주어질 때, 지뢰가 있는 칸을 제외한 다른 모든 칸의 숫자들이 표시되려면 최소 몇 번의 클릭을 해야 하는지 구하는 프로그램을 작성하라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에 하나의 정수 N(1 ≤ N ≤ 300) 이 주어진다. 이는 지뢰 찾기를 하는 표의 크기가 N*N임을 나타낸다.
다음 N개의 줄의 i번째 줄에는 길이가 N인 문자열이 주어진다.
이 중 j번째 문자는 표에서 i번째 행 j번째 열에 있는 칸이 지뢰가 있는 칸인지 아닌지를 나타낸다.
'*'이면 지뢰가 있다는 뜻이고, '.'이면 지뢰가 없다는 뜻이다. '*'와 '.'외의 다른 문자는 입력으로 주어지지 않는다.

[출력]
각 테스트 케이스마다 '#x'(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
최소 몇 번의 클릭을 해야 지뢰가 없는 모든 칸에 숫자가 표시될 것인지 출력한다.
"""

#8방향 bfs
from collections import deque

dirs = ((0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1))

#현재 기준 8방향에 지뢰 수 세기
def count_boom(i, j):
    cnt_boom = 0

    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]

        if 0 <= ni < n and 0 <= nj < n:
            if arr[ni][nj] == '*':
                cnt_boom += 1

    return cnt_boom


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    q = deque()
    cnt = 0

    for i in range(n):
        for j in range(n):

            #미확인 안전지대 확인
            if arr[i][j] != "*" and not visited[i][j]:
                cnt_boom = count_boom(i, j)

                #주변에 없으면 여기부터 터짐
                if cnt_boom == 0:
                    q.append((i, j))
                    visited[i][j] = True
                    cnt += 1

                    while q:
                        ci, cj = q.popleft()
                        
                        #더 퍼질 수 없으면 컷
                        if count_boom(ci, cj) != 0:
                            continue
                        
                        for dir in dirs:
                            ni, nj = ci + dir[0], cj + dir[1]
                            
                            if 0 <= ni < n and 0 <= nj < n:
                                if arr[ni][nj] != '*' and not visited[ni][nj]:
                                    visited[ni][nj] = True
                                    q.append((ni, nj))
    
    #방문처리 안된 친구들 1개씩 눌러
    for i in range(n):
        for j in range(n):
            if arr[i][j] != "*" and not visited[i][j]:
                cnt += 1

    print(f"#{tc} {cnt}")