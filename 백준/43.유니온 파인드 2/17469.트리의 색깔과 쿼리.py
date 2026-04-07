"""
N개의 정점으로 구성된 트리가 있다. 각 정점은 1번부터 N번까지 번호가 매겨져있고, 1 이상 10만 이하의 자연수로 표현되는 색깔을 하나 갖고 있다. 루트는 1번 정점이고, 트리이기 때문에 임의의 서로 다른 두 정점을 잇는 경로는 반드시 한 개 존재한다.
정점 u와 v를 잇는 경로가 존재하면 u에서 v로 갈 수 있다고 하자.
여러분은 아래 두 가지 쿼리를 처리해야 한다.
1 a : 정점 a와 a의 부모 정점을 연결하는 간선을 제거한다. (해당 간선이 존재하는 경우에만 주어진다.)
2 a : 정점 a에서 갈 수 있는 정점들만 보았을 때, 색깔의 종류의 개수를 출력한다.

#입력
첫 번째 줄에는 정점의 개수 N(1 ≤ N ≤ 100,000)과 2번 쿼리의 개수 Q(1 ≤ Q ≤ 1,000,000)가 주어진다.
다음 N-1개 줄의 i번째 줄에는 정점 i+1의 부모 정점을 나타내는 정수 p(1 ≤ p ≤ N)가 주어진다.
다음 N개 줄의 i번째 줄에는 정점 i의 색깔을 나타내는 정수 c(1 ≤ c ≤ 100,000)가 주어진다.
다음 N+Q-1개의 줄에는 여러분이 처리해야 할 쿼리가 주어지는데, 1번 쿼리는 N-1개, 2번 쿼리는 Q개 주어진다.
쿼리는 한 줄에 하나씩 쿼리의 종류를 나타내는 X(1 ≤ X ≤ 2)와 쿼리에서 처리할 정점의 번호 a(1 ≤ a ≤ N)가 주어진다.
입력은 모두 자연수로 주어진다.

#출력
Q개의 2번 쿼리에 대한 답을 순서대로 한 줄에 하나씩 출력한다.
"""

#쿼리를 역순 처리 할 것
# 끊는다 > 연결한다로 바꿔 처리

def find(x, uf_parent):
    while x != uf_parent[x]:
        uf_parent[x] = uf_parent[uf_parent[x]]
        x = uf_parent[x]
    return x

#대표 부모 연결 + 색집합 합치기
def union(a, b, sets):
    ra = find(a, uf_parent)
    rb = find(b, uf_parent)

    #작은 놈을 큰 놈에 합치기
    if ra != rb:
        if len(sets[ra]) < len(sets[rb]):
            ra, rb = rb, ra

        uf_parent[rb] = ra
        sets[ra] |= sets[rb]

import sys
input = sys.stdin.readline

n, q = map(int, input().split())

#원래 부모 노드 저장
tree_parent = list(range(n + 1))
for i in range(2, n + 1):
    a = int(input().rstrip())
    tree_parent[i] = a

#각 노드별 색을 담을 예정
sets = [set() for _ in range(n + 1)]
for j in range(1, n + 1):
    color = int(input().rstrip())
    sets[j].add(color)

#저장 후 역순 처리 할 예정
queries = [list(map(int, input().split())) for _ in range(n + q - 1)]

#문제에서 연결할 부모와 구분하기 위해 이렇게 작명
uf_parent = list(range(n + 1))
ans = []

#역순 처리
for cmd, node in reversed(queries):
    #부모 노드와 연결
    if cmd == 1:
        union(node, tree_parent[node], sets)
    
    #현재 노드가 속한 컴포넌트의 색 개수 확인
    else:
        root = find(node, uf_parent)
        ans.append(len(sets[root]))

#출력을 역순으로 해야 맞음
for i in ans[::-1]:
    print(i)