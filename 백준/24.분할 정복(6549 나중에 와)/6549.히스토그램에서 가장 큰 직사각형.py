"""
히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다.
히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

#입력
입력은 테스트 케이스 여러 개로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000) 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다. 이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다. 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

#출력
각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.
"""

#어 일단 스택으로 했어
#어 분할정복 아이디어 떠오르면 다시와
import sys

while True:
    arr = list(map(int, input().split()))

    if arr[0] == 0:
        break
    
    n = arr[0]
    stack = []
    ans = 0

    for i in range(1, n+1):
        start = i

        while stack and stack[-1][1] > arr[i]:
            a, val = stack.pop()
            start = a
            ans = max(ans, (val * (i - start)))
        
        stack.append((start, arr[i]))
    
    while stack:
        a, val = stack.pop()
        ans = max(ans, (val * (n - a + 1)))

    print(ans)