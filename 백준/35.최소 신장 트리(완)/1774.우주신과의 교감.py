"""
황선자씨는 우주신과 교감을 할수 있는 채널러 이다. 하지만 우주신은 하나만 있는 것이 아니기때문에 황선자 씨는 매번 여럿의 우주신과 교감하느라 힘이 든다. 이러던 와중에 새로운 우주신들이 황선자씨를 이용하게 되었다.
하지만 위대한 우주신들은 바로 황선자씨와 연결될 필요가 없다. 이미 황선자씨와 혹은 이미 우주신끼리 교감할 수 있는 우주신들이 있기 때문에 새로운 우주신들은 그 우주신들을 거쳐서 황선자 씨와 교감을 할 수 있다.
우주신들과의 교감은 우주신들과 황선자씨 혹은 우주신들 끼리 이어진 정신적인 통로를 통해 이루어 진다. 하지만 우주신들과 교감하는 것은 힘든 일이기 때문에 황선자씨는 이런 통로들이 긴 것을 좋아하지 않는다. 왜냐하면 통로들이 길 수록 더 힘이 들기 때문이다.
또한 우리들은 3차원 좌표계로 나타낼 수 있는 세상에 살고 있지만 우주신들과 황선자씨는 2차원 좌표계로 나타낼 수 있는 세상에 살고 있다. 통로들의 길이는 2차원 좌표계상의 거리와 같다.
이미 황선자씨와 연결된, 혹은 우주신들과 연결된 통로들이 존재한다. 우리는 황선자 씨를 도와 아직 연결이 되지 않은 우주신들을 연결해 드려야 한다. 새로 만들어야 할 정신적인 통로의 길이들이 합이 최소가 되게 통로를 만들어 “빵상”을 외칠수 있게 도와주자.

#입력
첫째 줄에 우주신들의 개수 N (1 ≤ N ≤ 1000) 이미 연결된 신들과의 통로의 개수 M (1 ≤ M ≤ 1000)가 주어진다.
두 번째 줄부터 N개의 줄에는 행성좌표를 포함하여 우주신들의 좌표 X, Y (0 ≤ X, Y ≤ 1000000)가 주어진다. 그 다음으로 M개의 줄에는 이미 연결된 통로가 주어진다. 번호는 위의 입력받은 좌표들의 순서라고 생각하면 된다. 좌표는 정수이다.

#출력
첫째 줄에 만들어야 할 최소의 통로 길이를 소수점 둘째 자리까지 반올림하여 출력하라.
"""

#1. 크루스칼
import sys
input = sys.stdin.readline

def kruskal(v, edges):
    parent = list(range(v+1))
    rank = [0] * (v+1)
    
    #재귀버전 find
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    #반복문버전 find
    def find2(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return False
        
        #ra의 랭크가 무조건 크다고 생각하고싶다.
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

n, m = map(int, input().split())

#먼저 우주신들의 좌표를 순서대로 받고
point = []
for _ in range(n):
    a, b = map(int, input().split())
    point.append((a, b))

#좌표를 통해 각 우주신들의 거리 계산해서 넣기
edges = []
for i in range(n):
    for j in range(i+1, n):
        d = float(((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2) ** 0.5)
        edges.append((d, i+1, j+1))

#이미 연결된 신들 번호를 받고, 그 거리를 0으로 하여 저장
for _ in range(m):
    c, d = map(int, input().split())
    edges.append((0, c, d))

total, cnt = kruskal(n, edges)
print(f"{total:.2f}")

#2. 프림
import sys
import heapq
input = sys.stdin.readline

def prim(v, graph, start=1):
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

n, m = map(int, input().split())

point = []
for _ in range(n):
    x, y = map(int, input().split())
    point.append((x, y))

#4386처럼 나누지 않고 한번에 그래프 생성
graph = [[] for _ in range(n+1)]
for i in range(n):
    for j in range(i+1, n):
        d = float(((point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2) ** 0.5)
        graph[i+1].append((d, j+1))
        graph[j+1].append((d, i+1))

#비용 0인 간선 처리도 해주고
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((0, b))
    graph[b].append((0, a))

total, cnt = prim(n, graph)
print(f"{total:.2f}")