"""
N개의 수 A1, A2, ..., AN과 L이 주어진다.
Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

#입력
첫째 줄에 N과 L이 주어진다. (1 ≤ L ≤ N ≤ 5,000,000)
둘째 줄에는 N개의 수 Ai가 주어진다. (-109 ≤ Ai ≤ 109)

#출력
첫째 줄에 Di를 공백으로 구분하여 순서대로 출력한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
for i in range(n):

    #넣을 때 덱 맨 뒤 값이 지금 값보다 크면 그거 제거 
    while q and q[-1] > arr[i]:
        q.pop()
    q.append(arr[i])

    #구간 범위 벗어나면 앞에서 제거
    if i >= l and q[0] == arr[i-l]:
        q.popleft()
    
    #맨 앞놈이 최소값임
    print(q[0], end = " ")