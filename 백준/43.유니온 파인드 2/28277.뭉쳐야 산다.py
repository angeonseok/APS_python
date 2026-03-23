"""
N개의 집합 S1, S2, …, SN이 주어질 때 다음 명령들을 Q개 처리해 보자.
1 a b: 집합 Sa를 Sa ∪ Sb로 바꾸고, Sb는 공집합으로 바꾼다. (1 ≤ a, b ≤ N; a ≠ b)
2 a: 집합 Sa의 크기를 출력한다. (1 ≤ a ≤ N)

#입력
첫 번째 줄에 N과 Q가 주어진다. (1 ≤ N, Q ≤ 500,000)
다음 N개 줄의 i 번째 줄에는 집합 Si의 정보가 주어진다.
각 줄에는 Si의 크기 ni가 먼저 주어지고, 이어서 Si의 원소 sij가 주어진다. (1 ≤ ∑ ni ≤ 500,000; 1 ≤ sij ≤ 109; 모든 k ≠ j에 대해 sij ≠ sik)
다음 Q개 줄에는 위에서 설명한 명령이 한 줄에 하나씩 주어진다.
입력되는 모든 수는 정수이고, 명령 2 a는 하나 이상 주어진다.

#출력
명령 2 a가 주어질 때마다 각 줄에 명령의 결과를 출력한다.
"""

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
sets = [set() for _ in range(n+1)]  #처음에 뭔 소린지 몰랐다. 집합을 만들자

for i in range(1, n + 1):
    arr = list(map(int, input().split()))

    for j in arr[1:]:
        sets[i].add(j)

for i in range(q):
    cmd = list(map(int, input().split()))

    #출력을 먼저 했네
    if cmd[0] == 2:
        print(len(sets[cmd[1]]))
    
    else:
        a = cmd[1]
        b = cmd[2]

        #유니온 파인드 랭크기준 합치기처럼
        #실제 집합의 크기 기준으로 큰 놈에 작은 놈을 합쳤네
        #합치고 작은 쪽은 공집합으로 만들었네
        if len(sets[a]) < len(sets[b]):
            sets[a], sets[b] = sets[b], sets[a]
        
        sets[a].update(sets[b])
        sets[b].clear()