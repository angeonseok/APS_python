"""
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

#출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
"""

import sys
input = sys.stdin.readline

n,s = map(int, input().split())
arr = list(map(int, input().split()))

#투포인터
r, l = 0, 0
sum_num = 0

#최솟값을 찾아보자
ans = 9876543210

while r < n:
    sum_num += arr[r]
    r += 1

    #만약 구간합이 원하는 값을 넘었다면
    while sum_num >= s:
        ans = min(r - l, ans)   #최소길이를 찾을 때 까지
        sum_num -= arr[l]       #l값을 늘려
        l+= 1

#합을 만족하는 수가 없다면 0을 출력
if ans == 9876543210 :
    print(0)
else:
    print(ans)