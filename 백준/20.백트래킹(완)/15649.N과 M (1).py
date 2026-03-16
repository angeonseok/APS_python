"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

#입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

#출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

import sys
input = sys.stdin.readline
n, m = map(int,input().split())

#중복 사용 방지
visited = [0] * (n + 1)

#현재 만들고 있는 순열 저장
permutation = []


def dfs(depth):
    
    #종료 조건
    if depth == m:
        print(*permutation)
        return
    
    #1~n까지 전부 후보로
    for i in range(1, n + 1):
        if not visited[i]:

            #선택
            visited[i] = 1
            permutation.append(i)

            #다음 단계
            dfs(depth + 1)

            #복구
            permutation.pop()
            visited[i] = 0

#처음엔 아무것도 선택 안했으니 0
dfs(0)