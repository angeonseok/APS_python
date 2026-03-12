"""
때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.
행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다. 

#출력
첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.
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
    
    def find2(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
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

            if cnt == v-1:
                break
    
    return total, cnt

n = int(input())

#edge 생성할때 n 수 안보고 전부 연결시키다가 메모리 터짐
#문제에서 거리는 3개의 축 중 차가 최소인 것으로 줘서 x,y,z 순으로 정렬해서 인접한 애들만 연결함
#일단 그러니 풀림

#포인트 저장할 때, 이 포인트가 몇번째 행성인지도 저장해야됨.
#정렬하고 이 포인트가 어느 행성인지 알아야지.
point = []
for i in range(n):
    x, y, z = map(int, input().split())
    point.append((x,y,z,i+1))

edges = []
#1. x정렬기준 인접한 애들 연결
point.sort(key=lambda x : x[0])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(x1 - x2)
    edges.append((d, a, b))

#2. y정렬 기준 인접한 애들 연결
point.sort(key=lambda x : x[1])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(y1 - y2)
    edges.append((d, a, b))

#3. z정렬 기준 인접한 애들 연결
point.sort(key=lambda x : x[2])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(z1 - z2)
    edges.append((d, a, b))

total, cnt = kruskal(n, edges)
print(total)

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

point = []
for i in range(n):
    x, y, z = map(int, input().split())
    point.append((x,y,z,i+1))

graph = [[] for _ in range(n+1)]

#x기준 정렬 후 인접한 행성 간 연결
point.sort(key=lambda x : x[0])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(x1-x2)
    graph[a].append((d, b))
    graph[b].append((d, a))

#y기준 정렬 후 인접한 행성 간 연결
point.sort(key=lambda x : x[1])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(y1-y2)
    graph[a].append((d, b))
    graph[b].append((d, a))

#z기준 정렬 후 인접한 행성 간 연결
point.sort(key=lambda x : x[2])
for i in range(n-1):
    x1, y1, z1, a = point[i]
    x2, y2, z2, b = point[i+1]
    d = abs(z1-z2)
    graph[a].append((d, b))
    graph[b].append((d, a))

total, cnt = prim(n, graph)
print(total)