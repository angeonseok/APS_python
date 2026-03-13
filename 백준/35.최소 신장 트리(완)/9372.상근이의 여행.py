"""
상근이는 겨울방학을 맞아 N개국을 여행하면서 자아를 찾기로 마음먹었다. 
하지만 상근이는 새로운 비행기를 무서워하기 때문에, 최대한 적은 종류의 비행기를 타고 국가들을 이동하려고 한다.
이번 방학 동안의 비행 스케줄이 주어졌을 때, 상근이가 가장 적은 종류의 비행기를 타고 모든 국가들을 여행할 수 있도록 도와주자.
상근이가 한 국가에서 다른 국가로 이동할 때 다른 국가를 거쳐 가도(심지어 이미 방문한 국가라도) 된다.

#입력
첫 번째 줄에는 테스트 케이스의 수 T(T ≤ 100)가 주어지고,
각 테스트 케이스마다 다음과 같은 정보가 주어진다.
첫 번째 줄에는 국가의 수 N(2 ≤ N ≤ 1 000)과 비행기의 종류 M(1 ≤ M ≤ 10 000) 가 주어진다.
이후 M개의 줄에 a와 b 쌍들이 입력된다. a와 b를 왕복하는 비행기가 있다는 것을 의미한다. (1 ≤ a, b ≤ n; a ≠ b) 
주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.

#출력
테스트 케이스마다 한 줄을 출력한다.
상근이가 모든 국가를 여행하기 위해 타야 하는 비행기 종류의 최소 개수를 출력한다.
"""

#1. 크루스칼
import sys
input = sys.stdin.readline

def kruskal(v, edges):

    #rank기준으로 union 할거임
    parent = list(range(v+1))
    rank = [0] * (v + 1)

    #크루스칼은 유니온 파인드로 사이클 생기나 체크하면서 간선 고른다.
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    #반복문버전도 알아둬라
    # def find(x):
    #     while parent[x] != x:
    #         parent[x] = parent[parent[x]]
    #         x = parent[x]
    #     return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        
        else:
            parent[rb] = ra
            rank[ra] += 1

        return True
    
    #비용기준으로 정렬
    edges.sort()
    total = 0
    cnt = 0       #선택한 간선 수 카운팅

    #싼 간선부터 보면서 합칠 수 있으면 채택
    for w, a, b in edges:
        if union(a, b):
            total += w
            cnt += 1

            #간선 v-1개면 트리 완성이라 더 볼 필요없다.
            if cnt == v - 1:
                break
    
    return total, cnt

T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    edges = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((0, a, b))
    
    total, cnt = kruskal(n, edges)

    print(cnt)

#2. 프림
import sys
import heapq
input = sys.stdin.readline

def prim(v, graph, start=1):
    visited = [False] * (v+1)
    pq = [(0, start)]
    total = 0
    cnt = 0         #mst에 포함된 정점 개수

    #힙 내용물 꺼내면서
    while pq and cnt < v:
        w, u = heapq.heappop(pq)
        
        #방문한 노드에 대해서는 처리 x
        if visited[u]:
            continue

        #방문처리하고 거리 합치기
        visited[u] = True
        total += w 
        cnt += 1

        #정접과 연결된 다른 정점들 중 방문 안한거 있으면 힙에 담기
        for nw, nu in graph[u]:
            if not visited[nu]:
                heapq.heappush(pq, (nw, nu))

    #그래프가 연결이면 cnt == v 아니면 문제가 있다.
    return total, cnt

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append((0,b))
        graph[b].append((0,a))
    
    total, cnt = prim(n, graph)
    print(cnt-1)