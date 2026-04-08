"""
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

#입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

#출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
"""

import sys
input = sys.stdin.readline

def mat_mul(a, b):
    mat = [[0] * n for _ in range(n)]

    #행렬 계산 후 나머지를 += 로 갈겼다가 이상하게 나옴
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat[i][j] = (mat[i][j] + a[i][k] * b[k][j]) % 1000

    return mat

#즐거운 분할정복
def div_mat_cal(arr, b):

    #길이가 1이 된 경우 일단 모든 항목을 1000으로 나눈 나머지로
    if b == 1:
        for i in range(n):
            for j in range(n):
                arr[i][j] %= 1000
        return arr

    #거듭제곱횟수가 짝수면 반갈
    if b % 2 == 0:
        m_half = div_mat_cal(arr, b//2)
        return mat_mul(m_half, m_half)

    #홀수면 반갈반갈 계산 후 하나 따로 더 계산
    else:
        m_half = div_mat_cal(arr, b//2)
        return mat_mul(mat_mul(m_half, m_half), arr)
    

n, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = div_mat_cal(arr, b)
for i in ans:
    print(*i)