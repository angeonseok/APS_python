"""
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.
이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.
이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

#입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

#출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

link = [0] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)  #b > a로 해킹가능

for i in range(1, n+1):
    q = deque()
    visited = [-1] * (n+1)
    cnt = 1
    
    q.append(i)
    visited[i] = 0
    while q:
        x = q.popleft()
        
        #현재 컴퓨터에서 해킹가능한 컴퓨터 수 카운팅
        for nx in graph[x]:
            if visited[nx] == -1:
                visited[nx] = 1
                cnt += 1
                q.append(nx)

    #결과 저장
    link[i] = cnt

#최대로 해킹할 수 있는 컴퓨터를 골라보자
max_link = max(link)

#여러개면 오름차순 출력
for j in range(1, n+1):
    if link[j] == max_link:
        print(j, end = " ")