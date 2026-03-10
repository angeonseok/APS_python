"""
초기에 ( n + 1 )개의 집합 ({0}, {1}, {2}, \dots, {n})이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
집합을 표현하는 프로그램을 작성하시오.

#입력
첫째 줄에 (n, m)이 주어진다. (m)은 입력으로 주어지는 연산의 개수이다. 다음 (m)개의 줄에는 각각의 연산이 주어진다. 합집합은 `0 a b`의 형태로 입력이 주어진다. 이는 (a)가 포함되어 있는 집합과, (b)가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 `1 a b`의 형태로 입력이 주어진다. 이는 (a)와 (b)가 같은 집합에 포함되어 있는지를 확인하는 연산이다.

#출력
1로 시작하는 입력에 대해서 (a)와 (b)가 같은 집합에 포함되어 있으면 `"YES"` 또는 `"yes"`를, 그렇지 않다면 `"NO"` 또는 `"no"`를 한 줄에 하나씩 출력한다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#자기 자신을 부모로 시작해보자
parent = [i for i in range(n+1)]

#x의 루트를 경로를 압축하면서 찾자
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

#서로의 루트가 다를 경우 통합하자(b루트를 a루트 밑으로)
def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA

for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)

    else:
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            print("yes")
        else:
            print("no")