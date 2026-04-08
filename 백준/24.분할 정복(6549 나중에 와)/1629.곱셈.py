"""
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

#출력
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
"""

#숫자 크게 곱하면 터져서 매 계산마다 나눔
def mul_mod(a, b, c):
    if b == 0:
        return 1 % c
    
    #C^n = C^(n/2) * C^(n/2)
    if b % 2 == 0:
        n_b = mul_mod(a, b // 2, c)
        return (n_b * n_b) % c
    
    #C^n = C^(n/2) * C^(n/2) * C
    else:
        n_b = mul_mod(a, (b-1) // 2, c)
        return ((n_b * n_b) % c) * a % c
    
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(mul_mod(a, b, c))