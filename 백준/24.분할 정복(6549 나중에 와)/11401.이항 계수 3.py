"""
자연수 N과 정수 K가 주어졌을 때 이항계수 nCk를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 N과 K 가 주어진다. (1 ≤ N ≤ 4,000,000, 0 ≤ K ≤ N)

#출력
nCk를 1,000,000,007로 나눈 나머지를 출력한다.
"""

import sys
input = sys.stdin.readline

mod = 1000000007

#거듭제곱 계산을 위한 함수
def power_div_mod(a, b, mod):
    if b == 0:
        return 1 % mod

    if b % 2 == 0:
        half = power_div_mod(a, b //2 , mod)
        return (half * half) % mod
    
    else:
        half = power_div_mod(a, (b-1) // 2, mod)
        return ((half * half) % mod) * a % mod
    

def com(n, r, mod):

    #조합 생성 자체가 불가능
    if r < 0 or r > n:
        return 0
    
    #계산에 팩토리얼 들어감
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i-1] * i) % mod


    # nCr = n! / (r!(n-r)!) 이지만
    # mod 연산에서는 일반적인 나눗셈이 불가능하므로
    # 분모 r!(n-r)!의 "모듈러 역원"을 곱하는 방식으로 계산해야 한다.
    
    # mod가 소수일 때 페르마의 소정리에 의해
    # a^(mod-1) ≡ 1 (mod mod)   (단, a는 mod의 배수가 아님)
    # 따라서 a^(mod-2) ≡ a^(-1) (mod mod)
    # 즉, a의 역원은 a^(mod-2) % mod 로 구할 수 있다.
    
    # 그래서
    # nCr % mod
    # = n! * (r!(n-r)!)^(-1) % mod
    # = n! * (r!(n-r)!)^(mod-2) % mod

    return (fact[n] * power_div_mod(fact[r]*fact[n-r], mod-2, mod)) % mod

n, k = map(int, input().split())
ans = com(n, k, mod)
print(ans)