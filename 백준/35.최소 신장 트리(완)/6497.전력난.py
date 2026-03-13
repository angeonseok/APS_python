"""
성진이는 한 도시의 시장인데 거지라서 전력난에 끙끙댄다. 그래서 모든 길마다 원래 켜져 있던 가로등 중 일부를 소등하기로 하였다. 길의 가로등을 켜 두면 하루에 길의 미터 수만큼 돈이 들어가는데, 일부를 소등하여 그만큼의 돈을 절약할 수 있다.
그러나 만약 어떤 두 집을 왕래할 때, 불이 켜져 있지 않은 길을 반드시 지나야 한다면 위험하다. 그래서 도시에 있는 모든 두 집 쌍에 대해, 불이 켜진 길만으로 서로를 왕래할 수 있어야 한다.
위 조건을 지키면서 절약할 수 있는 최대 액수를 구하시오.

#입력
입력은 여러 개의 테스트 케이스로 구분되어 있다.
각 테스트 케이스의 첫째 줄에는 집의 수 m과 길의 수 n이 주어진다. (1 ≤ m ≤ 200000, m-1 ≤ n ≤ 200000)
이어서 n개의 줄에 각 길에 대한 정보 x, y, z가 주어지는데, 이는 x번 집과 y번 집 사이에 양방향 도로가 있으며 그 거리가 z미터라는 뜻이다. (0 ≤ x, y < m, x ≠ y)
도시는 항상 연결 그래프의 형태이고(즉, 어떤 두 집을 골라도 서로 왕래할 수 있는 경로가 있다), 도시상의 모든 길의 거리 합은 231미터보다 작다.
입력의 끝에서는 첫 줄에 0이 2개 주어진다.

#출력
각 테스트 케이스마다 한 줄에 걸쳐 절약할 수 있는 최대 비용을 출력한다.
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

#입력양식 안지켰다가 틀림
while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break
    
    #전체 비용 - 최소 연결 비용 = 최대 절약 비용
    t_cost = 0

    edges = []
    for _ in range(n):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))
        t_cost += w

    total, cnt = kruskal(m, edges)
    print(t_cost-total)

#2. 프림
import sys
import heapq
input = sys.stdin.readline

#문제마다 시작번호를 잘 봐야 할 듯. 이번 문제는 시작번호가 0번
def prim(v, graph, start=0):
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

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break
    
    t_cost = 0
    graph = [[] for _ in range(m+1)]
    for _ in range(n):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
        t_cost += w
    
    total , cnt = prim(m, graph)
    print(t_cost-total)
