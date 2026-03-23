"""
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

#출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

#그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#방문 체크 + 부모노드 저장용 리스트 생성
visited = [0] * (n+1)
p = [0] * (n+1)

#루트를 1로 설정
q = deque([1])
visited[1] = -1

#bfs로 순회하면서 a의 자식들 체크 > 자식들의 자식 체크 .............
while q:
    a = q.popleft()
    for i in graph[a]:
        if visited[i] == 0:
            visited[i] = -1
            p[i] = a
            q.append(i)

for i in p:
    if i != 0:
        print(i)