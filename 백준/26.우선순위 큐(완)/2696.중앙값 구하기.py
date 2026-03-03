"""
어떤 수열을 읽고, 홀수번째 수를 읽을 때 마다, 지금까지 입력받은 값의 중앙값을 출력하는 프로그램을 작성하시오.
예를 들어, 수열이 1, 5, 4, 3, 2 이면, 홀수번째 수는 1번째 수, 3번째 수, 5번째 수이고, 1번째 수를 읽었을 때 중앙값은 1, 3번째 수를 읽었을 때는 4, 5번째 수를 읽었을 때는 3이다.

#입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스의 첫째 줄에는 수열의 크기 M(1 ≤ M ≤ 9999, M은 홀수)이 주어지고, 그 다음 줄부터 이 수열의 원소가 차례대로 주어진다. 원소는 한 줄에 10개씩 나누어져있고, 32비트 부호있는 정수이다.

#출력
각 테스트 케이스에 대해 첫째 줄에 출력하는 중앙값의 개수를 출력하고, 둘째 줄에는 홀수 번째 수를 읽을 때 마다 구한 중앙값을 차례대로 공백으로 구분하여 출력한다. 이때, 한 줄에 10개씩 출력해야 한다.
"""

import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    #입력 양식이 10개씩 들어온다
    arr = []
    r = n
    while r > 0:
        line = list(map(int,input().split()))
        arr.extend(line)
        r -= len(line)

    #중앙값 기준 더 큰 놈을 min에, 중앙값 포함해서 작은 놈은 max에
    max_heap = []
    min_heap = []

    ans = []
    
    #길이가 같은 경우 max heap에 우선 넣기
    for i in range(n):
        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -arr[i])
        else:
            heapq.heappush(min_heap, arr[i])

        #넣은 후 조건 맞추기(중앙값은 max heap에 들어갈 수 있도록)
        if max_heap and min_heap and (-max_heap[0] > min_heap[0]):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        #순서기준 홀수번쨰 마다 중앙값 추출
        if i % 2  == 0:
            ans.append(-max_heap[0])

    #출력양식도 이상해오
    print(len(ans))
    for i in range(0, len(ans), 10):
        print(*ans[i:i+10])