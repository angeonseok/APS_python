"""
다음과 같이 Encoding 을 한다.
1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.
2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.
입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.

[제약사항]
문자열의 길이는 항상 4의 배수로 주어진다.
그리고 문자열의 길이는 100000을 넘지 않는다.

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스는 Encoding 된 상태로 주어지는 문자열이다.

[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

base_table ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

T = int(input())
for tc in range(1, T+1):
    s = input()

    binary = ""
    for i in s:
        #테이블에 저장된 문자의 인덱스를 구하고, 그것을 6자리 이진수로 변환
        binary += format(base_table.find(i), '06b')

    ans = ""
    for k in range(0, len(binary), 8):
        #8개씩 잘라서 만든 8자리 이진수를 10진법으로 변환한 후, 문자로 변환
        ans += chr(int(binary[k:k+8], 2))

    print(f"#{tc} {ans}")