"""
트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.

#입력
파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

#출력
첫째 줄에 트리의 지름을 출력한다.
"""

#1167번 문제와 풀이가 같음

import sys
from collections import deque
input = sys.stdin.readline

def bfs(root, graph):
    k = len(graph)
    
    q = deque()
    visited = [-1] * k
    q.append(root)
    visited[root] = 0

    while q:
        now = q.popleft()

        #그래서 dist만 이용해봤네
        for nxt, dist in graph[now]:
            if visited[nxt] == -1:
                visited[nxt] = visited[now] + dist
                q.append(nxt)

    far_node = 0
    far_dist = 0

    for i in range(1, k):
        if far_dist < visited[i]:
            far_dist = visited[i]
            far_node = i

    return far_node, far_dist
                
n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))
    graph[b].append((a, v))

a, b = bfs(n, graph)
c, d = bfs(a, graph)
print(d)