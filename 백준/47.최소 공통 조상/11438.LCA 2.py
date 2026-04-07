"""
N(2 ≤ N ≤ 100,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.
두 노드의 쌍 M(1 ≤ M ≤ 100,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

#입력
첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다. 그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

#출력
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.
"""

import sys
from collections import deque
import math
input = sys.stdin.readline

def bfs(root, graph, N):
    log = int(math.log2(N)) + 1

    # 각 노드 깊이
    depth = [-1] * (N+1)

    # parent[k][v] = v의 2^k번째 조상
    parent = [[0] * (N+1) for _ in range(log)]
              
    depth[root] = 0
    q = deque([root])

    # bfs로 깊이랑 바로 위 부모 먼저 구함
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if depth[nxt] == -1:
                depth[nxt] = depth[node] + 1
                parent[0][nxt] = node
                q.append(nxt)

    # parent 테이블 채우기
    # 2^k번째 조상 = 2^(k-1)번째 조상의 2^(k-1)번째 조상
    for k in range(1, log):
        for v in range(1, N+1):
            parent[k][v] = parent[k-1][parent[k-1][v]]
    
    return depth, parent, log

def lca(u, v, depth, parent, log):
    # 더 깊은 쪽을 u로 맞춤
    if depth[u] < depth[v]:
        u, v = v, u
    
    # 깊이 차이만큼 u를 먼저 끌어올림
    diff = depth[u] - depth[v]
    for k in range(log):
        if diff & (1 << k):
            u = parent[k][u]
    
    # 깊이 맞췄더니 같아지면 그게 lca
    if u == v:
        return u
    
    # 가장 큰 점프부터 보면서
    # 둘의 조상이 다를 때만 같이 올림
    for k in range(log - 1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]

    # 여기까지 오면 바로 위 부모가 lca
    return parent[0][u]


n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth, parent, log = bfs(1, graph, n)

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    lca_node = lca(u, v, depth, parent, log)
    print(lca_node)