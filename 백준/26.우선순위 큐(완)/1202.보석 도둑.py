"""
세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
모든 숫자는 양의 정수이다.

#출력
첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.
"""

import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())

#보석의 무게와 가치 저장
info = []
for _ in range(n):
    a, b = map(int, input().split())
    info.append((a,b))

#k개의 가방 수용가능 무게 저장
bag = []
for _ in range(k):
    c = int(input())
    bag.append(c)

#정렬
info.sort()
bag.sort()

heap = []
ans = 0
idx = 0

#작은 가방부터
for i in bag:
    
    #보석들 중 가방의 수용가능 무게보다 크지 않은 보석들을 찾고
    while idx < len(info) and info[idx][0] <= i:
        #보석의 가치를 최대 힙에 저장
        heapq.heappush(heap, -info[idx][1])
        idx += 1

    #가방 하나에 최대 가치 보석 하나씩 넣어서 합하기
    if heap:
        ans += -heapq.heappop(heap)

print(ans)