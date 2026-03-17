"""
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

#입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

#출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
"""

#인덱스를 잘 생각하자 한 번 틀렸다.
import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

n = len(str1) + 1
m = len(str2) + 1

#이차원 행렬을 만든다
dp = [[0] * n for _ in range(m)]

#예시기준
# \ 0 A C A Y K P
# 0 0 0 0 0 0 0 0
# C 0 0 1 1 1 1 1
# A 0 1 1 2 2 2 2
# P 0 1 1 2 2 2 3
# C 0 1 2 2 2 2 3
# A 0 1 2 3 3 3 3
# K 0 1 2 3 3 4 4

#채워넣을 예정
for i in range(1, m):
    for j in range(1, n):
        
        #두 문자가 같다면
        if str1[j-1] == str2[i-1]:

            #대각선 방향 기준 개수에서 +1한 값 저장
            dp[i][j] = dp[i-1][j-1] + 1
        
        #다르면
        else:

            #위나 왼쪽 중 큰 값을 저장해둔다
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[m-1][n-1])