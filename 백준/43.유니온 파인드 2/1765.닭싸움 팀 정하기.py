"""
닭싸움은 월드의 전통이다. 이번 캠프에서도 어김없이 닭싸움 대회가 열렸다. 그런데, 닭싸움을 하기 위해서는 반드시 누가 우리 편이고, 누가 우리 편이 아닌지를 알아야 할 것이다. 닭싸움의 팀을 정하는 원칙은, 평소 학생들의 인간관계에 따라 다음과 같이 정리할 수 있다.
내 친구의 친구는 내 친구이다.
내 원수의 원수도 내 친구이다.
이 때 두 학생이 친구이면 같은 팀에 속해있어야 하며, 같은 팀에 속해 있는 사람들끼리는 전부 친구여야 한다.
학생들의 인간관계가 주어지면, 닭싸움을 위한 팀 정하기를 할 때, 최대 얼마나 많은 팀이 만들어질 수 있는지 알아내는 프로그램을 작성하시오.

#입력
첫째 줄에 학생의 수 n이 주어진다. 각 학생들은 1부터 n까지 번호가 매겨져 있다. (2 ≤ n ≤ 1000) 
둘째 줄에 학생 간의 인간관계 중 알려진 것의 개수 m이 주어진다. (1 ≤ m ≤ 5000)
다음 m개의 줄에는 한 줄에 한 개씩, 학생 간의 인간관계가 F p q 혹은 E p q의 형태로 공백으로 구분되어 주어진다. (1 ≤ p < q ≤ n)
첫 번째 글자가 F인 경우에는 p와 q가 친구인 것이고, E인 경우는 p와 q가 원수인 경우이다. 
입력은 모순이 없음이 보장된다. 즉, 두 학생이 동시에 친구이면서 원수인 경우는 없다.

#출력
첫째 줄에, 가능한 최대 팀 개수를 출력한다.
"""

#관계를 xor 연산으로 처리할라다 꼬임
#걍 그래프로 적을 저장하면 되지 않겠나 했다가 마지막에 꼬임

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = list(range(n+1))
enemy = [[] for _ in range(n+1)]

for _ in range(m):
    rel, a, b = input().split()
    a = int(a)
    b = int(b)

    if rel == "F":
        union(a, b)
    
    else:
        enemy[a].append(b)
        enemy[b].append(a)

#모든 사람 보면서
for x in range(1, n+1):
    #나의 적을 찾고
    for e in enemy[x]:
        #나의 적의 적과
        for ee in enemy[e]:
            #합체
            union(x, ee)

#대표 기준으로 팀 개수 세기
team = set()
for i in range(1, n+1):
    team.add(find(i))

print(len(team))