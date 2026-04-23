"""
어떤 사화과학 연구 단체에서 사람의 네트워크에 대하여 여러 가지 측정 방법을 사용하여 연구하기로 하였다.
이를 위해 우선 주어진 사람 네트워크에서 누가 가장 영향력이 있는 사람인지를 알 수 있는 척도로서 다음을 분석하는 프로그램을 작성하시오.
단, N은 입력 사람 네트워크 (그래프)의 노드 수이다.
Closeness Centrality(CC):Closeness는 네트워크 상에서 한 사용자가 다른 모든 사람에게 얼마나 가까운가를 나타낸다.
 
[제약 사항]
입력으로 주어지는 사람 네트워크에서 노드 자신을 연결하는 간선은 없다.
또한 사람 네트워크는 하나의 연결 요소(connected component)로 구성되어 있다.
단, 사람 네트워크의 최대 사용자 수는 1,000 이하이다.
테스트 케이스들은 아래의 그룹들로 이루어져 있다.
그룹 1 싸이클이 없고 N <= 10 인 경우
그룹 2 싸이클이 없고 10 < N <= 100 인경우
그룹 3 싸이클이 있고 N<= 10
그룹 4 싸이클이 있고10 < N <= 100
그룹 5 모든 경우가 존재하고 100 < N <= 1000

[입력]
맨 위의 줄에는 전체 테스트 케이스의 수 T가 주어진다.
그 다음 줄부터 T개의 테스트 케이스가 주어진다.
각 테스트 케이스는 한 줄에 주어지며, 사람 수인 양의 정수 N이 주어진 다음, 사람 네트워크의 인접 행렬이 행 우선 (row-by-row) 순으로 주어진다.
단, 각 숫자 사이에는 1개의 공백이 주어진다.

[출력]
총 T줄에 T개의 테스트 케이스 각각에 대한 답을 한 줄에 출력한다.
각 줄은 '#x'로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 사람 그래프에서 사람들의 CC 값들 중에서 최솟값을 한 줄에 출력한다.
"""

#모든 정점 도달 거리의 합 구해야됨
INF = 10**18
 
def floyd(dist, n):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
 
            ik = dist[i][k]
 
            for j in range(n):
                nd = ik + dist[k][j]
                if nd < dist[i][j]:
                    dist[i][j] = nd
 
 
T = int(input())
for tc in range(1, T+1):
    tmp = list(map(int, input().split()))
 
    arr = tmp[1:]
    n = tmp[0]
 
    dist = []
    for i in range(0, len(arr), n):
        tmp = arr[i:i+n]
        dist.append(tmp)
     
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = INF
 
    floyd(dist, n)
     
    ans = min(sum(row) for row in dist)
    print(f"#{tc} {ans}")