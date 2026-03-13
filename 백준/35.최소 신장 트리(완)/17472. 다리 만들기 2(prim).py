#크루스칼에 주석 다 달아둠. prim방식으로 푸는 것만 적을 예정
import sys
import heapq
from collections import deque
input = sys.stdin.readline

dirs = ((0,1), (1,0),(0,-1),(-1,0))

def island(arr):
    q = deque()
    cnt = 1
    i_cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i,j))
                arr[i][j] += cnt
                cnt +=1
                i_cnt += 1

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


def bridge(arr):
    temp= []

    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cur_i = arr[i][j]

                for dir in dirs:
                    cnt = 0
                    ni, nj = i + dir[0], j + dir[1]

                    while 0 <= ni < n and 0 <= nj < m:
                        if arr[ni][nj] == cur_i:
                            break
                        
                        if arr[ni][nj] == 0:
                            cnt += 1
                            ni += dir[0]
                            nj += dir[1]
                            continue

                        if arr[ni][nj] != 0 and arr[ni][nj] != cur_i:
                            c = arr[ni][nj]
                            if cnt >= 2:
                                temp.append((cnt, cur_i, c))
                            break                    
    graph = e_to_g(temp)
    return graph


#중복제거 + 그래프 변환
def e_to_g(edges):
    e_dict = {}
    for w, a, b in edges:
        a, b = min(a, b), max(a, b)
        if (a, b) not in e_dict or w < e_dict[(a, b)]:
            e_dict[(a, b)] = w
    
    l = len(edges)
    graph = [[] for _ in range(i_cnt + 2)]
    for (a, b), w in e_dict.items():
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    return graph



#시작정점이 2
def prim(v, graph, start = 2):
    visited = [False] * len(graph)
    pq = [(0, start)]
    total = 0
    cnt = 0

    while pq and cnt < v:
        w, u = heapq.heappop(pq)

        if visited[u]:
            continue
        visited[u] = True
        total += w
        cnt += 1

        for nw, nu in graph[u]:
            if not visited[nu]:
                heapq.heappush(pq,(nw,nu))

    return total, cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr, i_cnt = island(arr)
graph = bridge(arr)
total, cnt = prim(i_cnt, graph)

#prim은 cnt를 연결된 정점 수를 보내준다
if cnt != i_cnt:
    print(-1)
else:
    print(total)