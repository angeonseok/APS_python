# 주어진 텍스트를 그대로 출력하세요.

n=5
for i in range(n):
    print(('+' * i) + '#' + ('+' * (n - 1 - i)))