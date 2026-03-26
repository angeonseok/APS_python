"""
n(1 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.
모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.

#출력
먼저, n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
그 다음에는 n*n개의 줄을 출력해야 한다. i*n+j번째 줄에는 도시 i에서 도시 j로 가는 최소 비용에 포함되어 있는 도시의 개수 k를 출력한다. 그 다음, 도시 i에서 도시 j로 가는 경로를 공백으로 구분해 출력한다. 이때, 도시 i와 도시 j도 출력해야 한다. 만약, i에서 j로 갈 수 없는 경우에는 0을 출력한다.
"""

#기존 역추적들이 이전 값들을 저장했는데
#얘는 다음 경로 값을 저장해야되네
import sys
input = sys.stdin.readline

INF = 10**18

def floyd(n, dist, trace):
    for k in range(1, n+1):
        for i in range(1, n+1):
            if dist[i][k] == INF:
                continue

            for j in range(1, n+1):
                nd = dist[i][k] + dist[k][j]
            
                if dist[i][j] > nd:
                    dist[i][j] = nd
                    trace[i][j] = trace[i][k]   #다음 갈 노드 갱신

def route(i, j, trace):
    #애초에 못가거나, 자기 자신에게 가는 경우
    if trace[i][j] == 0:
        return []

    cur = i
    path = [i]

    #다음 노드 추적
    while cur != j:
        cur = trace[cur][j]
        path.append(cur)
    
    return path
    

n = int(input())
dist = [[INF] * (n + 1) for _ in range(n + 1)]
trace = [[0] * (n+1) for _ in range(n+1)]  

for i in range(1, n + 1):
    dist[i][i] = 0

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    
    if c < dist[a][b]:
        dist[a][b] = c
        trace[a][b] = b     #다음 위치 저장

floyd(n, dist, trace)

#따로 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

#여기도 dist값 안따지고 걍 path 생성 가능여부만으로 하니 좋네
for i in range(1, n+1):
    for j in range(1, n+1):
        path = route(i, j, trace)

        if path:
            print(len(path), *path)
        else:
            print(0)