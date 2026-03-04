"""
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.
세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

#입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

#출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
"""

import sys
import heapq
input = sys.stdin.readline

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]

#이번엔 양방향 그래프당
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

#경유지점 저장용
point = list(map(int,input().split()))

INF = 10**18

#3번 해야되기 떄문에 함수로 다익스트라 구현
def dijkstra(n, start, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0

    pq = [(0,start)]

    while pq:
        d, u = heapq.heappop(pq)

        if d != dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist

#시작점 > 모든 정점간 최소거리
d1 = dijkstra(n, 1, graph)

#경유지점 1 > 모든 정점간 최소거리
d2 = dijkstra(n, point[0], graph)

#경유지점 2 > 모든 정점 간 최소거리
d3 = dijkstra(n, point[1], graph)

#루트 1 : 시작점 > 경유지점 1 > 경유지점 2 > 목적지
route1 = d1[point[0]] + d2[point[1]] + d3[n]

#루트 2 : 시작점 > 경유지점 2 > 경유지점 1 > 목적지
route2 = d1[point[1]] + d3[point[0]] + d2[n]

ans = min(route1, route2)
if ans >= INF:
    print(-1)
else:
    print(ans)