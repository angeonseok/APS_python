"""
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

#출력
첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.
"""

import sys
input = sys.stdin.readline

mod = 1000000007

#검색좀 했음

# 피보나치 전이행렬:
# [F(n)  ]   [1 1] [F(n-1)]
# [F(n-1)] = [1 0] [F(n-2)]
# 따라서 [[1,1],[1,0]]^(n-1)의 [0][0]은 F(n)이다.
def mat_mul(a, b):
    mat = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                mat[i][j] = (mat[i][j] + a[i][k] * b[k][j]) % mod
    return mat

# 분할정복으로 행렬 거듭제곱 계산
# num == 0이면 A^0 = I 이므로 단위행렬 반환
def pibb(arr, num):
    if num == 0:
        return [[1, 0], [0, 1]]
    if num == 1:
        for i in range(2):
            for j in range(2):
                arr[i][j] %= mod
        return arr
    
    if num % 2 == 0:
        half = pibb(arr, num // 2)
        return mat_mul(half, half)
    else:
        half = pibb(arr, num // 2)
        return mat_mul(mat_mul(half, half), arr)
    
n = int(input())
arr = [[1, 1], [1, 0]]
ans = pibb(arr, n-1)
print(ans[0][0])