"""
초기에 {1}, {2}, ... {n} 이 각각 n개의 집합을 이루고 있다.
여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
연산을 수행하는 프로그램을 작성하시오.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫째 줄에 n(1≤n≤1,000,000), m(1≤m≤100,000)이 주어진다.
m은 입력으로 주어지는 연산의 개수이다.
다음 m개의 줄에는 각각의 연산이 주어진다.
합집합은 0 a b의 형태로 입력이 주어진다.
이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다.
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다.
이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
a와 b는 n 이하의 자연수이며 같을 수도 있다.

[출력]
각 테스트 케이스마다 1로 시작하는 입력에 대해서 같은 집합에 속해있다면 1을, 아니면 0을 순서대로 한줄에 연속하여 출력한다.
"""

#전형적인 유니온파인드

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
 
 
def union(a, b):
    ra = find(a)
    rb = find(b)
     
    if ra != rb:
        parent[rb] = ra
 
 
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    parent = list(range(n+1))
     
    ans = ""
    for _ in range(m):
        cmd, a, b = map(int, input().split())
 
        if cmd  == 0:
            union(a, b)
         
        else:
            if find(a) == find(b):
                ans += '1'
            else:
                ans += '0'
 
    print(f"#{tc} {ans}")