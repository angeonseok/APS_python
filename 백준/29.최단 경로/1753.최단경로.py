"""
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

#입력
첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

#출력
첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
"""

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

#그래프에 간선 가중치도 포함시키기
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w= map(int,input().split())
    graph[u].append((v,w))

#시작점 > 각 정점까지 최단 거리 정보 받기
INF = 10 ** 18
dist = [INF] * (V + 1)
dist[start] = 0

#(시작점과의 거리, 정점) 힙에 담기
pq = [(0,start)]

#다익스트라는 힙을 활용
while pq:
    d, u = heapq.heappop(pq)
    
    #dist는 최신 정보가 들어감. d와 dist가 다르면 구버전이니 스킵
    if d != dist[u]:
        continue
    
    #거리정보 갱신
    for v, w in graph[u]:
        nd = d + w

        #갱신 가능하면 힙에 다시 넣자
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

ans = []
for i in range(1, V+1):
    if dist[i] == INF:
        ans.append("INF")
    else:
        ans.append(str(dist[i]))

print("\n".join(ans))