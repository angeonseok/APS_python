"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

#입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

#출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#최소길이가 1임
dp = [1] * n

#i까지를 기준으로
for i in range(n):
    #i 이전 항에 대해
    for j in range(i):
        #arr[i]가 이전 항보다 크다면
        if arr[i] > arr[j]:
            #최대길이를 dp에 저장
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))