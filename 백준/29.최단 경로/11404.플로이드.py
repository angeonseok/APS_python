"""
n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.
모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.
시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

#출력
n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
"""

import sys
input = sys.stdin.readline

INF = 10**18

#dist[i][j] = i -> j 최단거리
#k를 중간에 거쳐도 되는 정점으로 하나씩 허용하며 업데이트
def floyd_warshall(n, dist):
    for k in range(1, n+1):
        for i in range(1, n+1):

            #애초에 i -> k가 불가능하면 무시
            if dist[i][k] == INF:
                continue

            ik = dist[i][k]

            #기존 경로 대비 우회경로가 더 빠르면 갱신
            for j in range(1, n+1):
                nd = ik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd


n = int(input())
m = int(input())

#거리 행렬 초기화
dist = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신 가는 비용은 0으로
for i in range(n + 1):
    dist[i][i] = 0

#입력 받은 애들 넣어주고
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c

#모든 쌍 최단거리 계산
floyd_warshall(n, dist)

#도달 불가한 경우 0으로 변환해서 출력
for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append("0" if dist[i][j] == INF else str(dist[i][j]))
    print(" ".join(row))
