"""
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.
어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

#입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

#출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    #사이즈도 계산해서 리턴시켜주기
    if root_a != root_b:
        parent[root_b] = root_a
        size[root_a] += size[root_b]
    return size[root_a]

T = int(input())
for _ in range(T):
    n = int(input())

    #문자열이라 딕셔너리가 떠오르더라
    parent = {}
    size = {}
    for i in range(n):
        a, b = map(str, input().split())
        
        #숫자로 줄떄는 for문으로 자기 자신 parent 등록하고 사이즈도 넣었는데..
        #딕셔너리로 받아서 해야하니 먼저 등록하고 union시키자
        if a not in parent:
            parent[a] = a
            size[a] = 1

        if b not in parent:
            parent[b] = b
            size[b] = 1

        print(union(a, b))