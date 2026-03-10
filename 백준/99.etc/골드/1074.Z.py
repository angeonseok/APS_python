"""
수는 크기가 2N * 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2*2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
(그림있음)
N > 1인 경우, 배열을 크기가 2N-1 * 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
다음 예는 22 * 22 크기의 배열을 방문한 순서이다.
(그림있음)
N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
다음은 N=3일 때의 예이다.
(그림있음)

#입력
첫째 줄에 정수 N, r, c가 주어진다.

#출력
r행 c열을 몇 번째로 방문했는지 출력한다.
"""

import sys
input = sys.stdin.readline

#처음엔 배열을 직접만들다가 시간 터짐
#주어진 좌표가 몇 사분면 안에 있는지 파악하면서 그 이외 영역 칸수 다 더함

def Z_arr(r, c, n):
    if n == 1:
        return 0
    
    half = n // 2
    area = half * half

    #1사분면
    if r < half and c < half:
        return Z_arr(r, c, half)
    
    #2사분면
    if r < half and c >= half:
        return area + Z_arr(r, c - half, half)
    
    #3사분면
    if r >= half and c < half:
        return 2 * area + Z_arr(r - half, c, half)
    
    #4사분면
    if r >= half and c >= half:
        return 3 * area + Z_arr(r - half, c - half, half)
    
n, r, c = map(int, input().split())
print(Z_arr(r, c, 2 ** n))