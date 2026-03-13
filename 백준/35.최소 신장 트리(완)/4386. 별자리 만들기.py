"""
도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.
1. 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
2. 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.

#입력
첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다. 좌표는 1000을 넘지 않는 양의 실수이다.

#출력
첫째 줄에 정답을 출력한다. 절대/상대 오차는 10-2까지 허용한다.
"""

#1. 크루스칼
import sys
input = sys.stdin.readline

def kruskal(v, edges):
    parent = list(range(v+1))
    rank = [0] * (v+1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    # def find(x):
    #     while parent[x] != x:
    #         parent[x] = parent[parent[x]]
    #         x = parent[x]
    #     return x

    def union(a, b):
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
        if union(a, b):
            total += w
            cnt += 1
            if cnt == v - 1:
                break

    return total, cnt

n = int(input())
point = []

for _ in range(n):
    a, b = map(float, input().split())
    point.append((a, b))

#가중치를 직접 계산해서 edge 생성
edges = []
for i in range(n):
    for j in range(i+1, n):
        d = ((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2) ** 0.5
        edges.append((d, i+1, j+1))

total, cnt = kruskal(n, edges)
print(f"{total:.2f}")

#2. 프림
import sys
import heapq
input = sys.stdin.readline

def prim(v, graph, start = 1):
    visited = [False] * (v+1)
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
                heapq.heappush(pq, (nw, nu))
    
    return total, cnt

n = int(input())

#크루스칼보다 더 힘들게 그래프 만든거 같은데..
point = []
for i in range(n):
    a, b = map(float, input().split())
    point.append((a, b))

#temp없이 그래프를 한번에 만드는게 더 좋을 듯
temp = []
for i in range(n):
    for j in range(i+1, n):
        d = ((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2) ** 0.5
        temp.append((d, i+1, j+1))

graph = [[] for _ in range(n+1)]
for d, a, b in temp:
    graph[a].append((d, b))
    graph[b].append((d, a))

total, cnt = prim(n, graph)
print(f"{total:.2f}")