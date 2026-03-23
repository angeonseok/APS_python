"""
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

#입력
트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.
먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

#출력
첫째 줄에 트리의 지름을 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

    
#(간선수, 누적거리) 식으로 저장할 예정. 지금 보니까 간선도 필요없어보이는데.. 걍 지워도 될 듯
def bfs(start, graph):
    n = len(graph)
    visited =  [-1] * n

    q = deque()
    q.append(start)

    visited[start] = (0, 0)

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if visited[nxt[0]] == -1:
                v = nxt[1]
                visited[nxt[0]] = (visited[now][0] + 1, visited[now][1] + v)
                q.append(nxt[0])

    far_node = 0
    far_dist = 0

    #제일 먼 노드와 그 거리를 반환
    for i in range(1, n):
        if visited[i] == -1:
            continue

        if visited[i][1] > far_dist:
            far_node = i
            far_dist = visited[i][1]
    
    return far_node, far_dist


V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    arr = list(map(int, input().split()))
    arr.pop()          #-1 제거
    p = arr[0]

    # (정점, 비용) 쌍으로 추가
    for i in range(1, len(arr), 2):
        graph[p].append((arr[i], arr[i + 1]))

#이 문제는 2번 돌려야됨
a, b = bfs(1, graph)    #루트(1)부터 해서 제일 먼 놈 찾고
c, d = bfs(a, graph)    #그 놈 기준으로 제일 먼 거리가 정답
print(d)