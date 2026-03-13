"""
섬으로 이루어진 나라가 있고, 모든 섬을 다리로 연결하려고 한다. 이 나라의 지도는 N×M 크기의 이차원 격자로 나타낼 수 있고, 격자의 각 칸은 땅이거나 바다이다.
섬은 연결된 땅이 상하좌우로 붙어있는 덩어리를 말하고, 아래 그림은 네 개의 섬으로 이루어진 나라이다. 색칠되어있는 칸은 땅이다.
(그림)
다리는 바다에만 건설할 수 있고, 다리의 길이는 다리가 격자에서 차지하는 칸의 수이다. 다리를 연결해서 모든 섬을 연결하려고 한다. 섬 A에서 다리를 통해 섬 B로 갈 수 있을 때, 섬 A와 B를 연결되었다고 한다. 다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안된다. 또, 다리의 길이는 2 이상이어야 한다.
다리의 방향이 중간에 바뀌면 안되기 때문에, 다리의 방향은 가로 또는 세로가 될 수 밖에 없다. 방향이 가로인 다리는 다리의 양 끝이 가로 방향으로 섬과 인접해야 하고, 방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접해야 한다.
섬 A와 B를 연결하는 다리가 중간에 섬 C와 인접한 바다를 지나가는 경우에 섬 C는 A, B와 연결되어있는 것이 아니다. 
아래 그림은 섬을 모두 연결하는 올바른 2가지 방법이고, 다리는 회색으로 색칠되어 있다. 섬은 정수, 다리는 알파벳 대문자로 구분했다.
(그림)
다음은 올바르지 않은 3가지 방법이다.
(그림) (그림) (그림)
다리가 교차하는 경우가 있을 수도 있다. 교차하는 다리의 길이를 계산할 때는 각 칸이 각 다리의 길이에 모두 포함되어야 한다. 아래는 다리가 교차하는 경우와 기타 다른 경우에 대한 2가지 예시이다.
(그림) (그림)
나라의 정보가 주어졌을 때, 모든 섬을 연결하는 다리 길이의 최솟값을 구해보자.

#입력
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. 둘째 줄부터 N개의 줄에 지도의 정보가 주어진다. 각 줄은 M개의 수로 이루어져 있으며, 수는 0 또는 1이다. 0은 바다, 1은 땅을 의미한다.

#출력
모든 섬을 연결하는 다리 길이의 최솟값을 출력한다. 모든 섬을 연결하는 것이 불가능하면 -1을 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

dirs = ((0,1), (1,0),(0,-1),(-1,0))

#1. 섬을 찾고 구분한다. 그 후 섬의 개수도 세자
def island(arr):
    q = deque()
    cnt = 1
    i_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i,j))
                arr[i][j] += cnt
                cnt +=1         #칠하는거랑
                i_cnt += 1      #실제 섬의 개수

                while q:
                    x, y = q.popleft()

                    for dir in dirs:
                        nx, ny = x + dir[0], y + dir[1]
                        if not(0 <= nx < n and 0 <= ny < m):
                            continue
                        if arr[nx][ny] == 1:
                            arr[nx][ny] = arr[x][y]
                            q.append((nx,ny))

    return arr, i_cnt


#2. 섬마다 다리를 놓을 수 있으면 놓자.
def bridge(arr):
    edges= []

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cur_i = arr[i][j]   #시작지점 설정

                for dir in dirs:    #한 방형으로 쭉
                    cnt = 0
                    ni, nj = i + dir[0], j + dir[1]

                    while 0 <= ni < n and 0 <= nj < m:
                        if arr[ni][nj] == cur_i:    #같은 섬이면 그 방향으로 탐색 안함
                            break
                            
                        if arr[ni][nj] == 0:        #바다인 경우
                            cnt += 1                #다리를 놓자
                            ni += dir[0]
                            nj += dir[1]
                            continue

                        if arr[ni][nj] != 0 and arr[ni][nj] != cur_i:   #다른 섬이면
                            c = arr[ni][nj]     #도착지점으로 놓고
                            if cnt >= 2:        #다리 길이가 2 이상이면 연결
                                edges.append((cnt, cur_i, c))
                            break                    
    
    #중복간선 제거
    edges = clean(edges)
    return edges


#번외. 중복간선 제거
def clean(edges):
    dict = {}
    for w, a, b in edges:
        a, b = min(a, b), max(a, b)
        if (a, b) not in dict or w < dict[(a, b)]:
            dict[(a, b)] = w
    
    new_edges = []
    for (a, b), w in dict.items():
        new_edges.append((w, a, b))
    
    return new_edges


#3.모든 섬을 최소비용으로 연결하자
#3-1. 크루스칼
def kruskal(v, edges):
    parent = list(range(v+1))
    rank = [0] * (v+1)

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a,b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return False
        
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra

        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True
    
    edges.sort()
    total = 0
    cnt = 0

    for w, a, b in edges:
        if union(a,b):
            total += w
            cnt += 1

            if cnt == v-1:
                break
    
    return total, cnt


#4. 계산을 하자.
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr, i_cnt = island(arr)
edges = bridge(arr)
total, cnt = kruskal(i_cnt+1, edges)

if cnt != i_cnt - 1:    #간선의 개수 = 섬의 개수 - 1 
    print(-1)           #저게 아니면 모든 섬이 연결되지 않은 것
else:
    print(total)