# N x N 행렬이 주어질 때, 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

#제약 사항
#N은 3이상 7이하이다.

#입력
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N이 주어지고, 다음 N 줄에는 N x N 행렬이 주어진다.

#출력
# 출력의 첫 줄은 '#t'로 시작하고, 다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.
# 입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

def t_90(arr, n):
    t_arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n-1,-1,-1):
            t_arr[i].append(arr[j][i])
    return t_arr

T = int(input())

for a in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    
    arr_90 = t_90(arr, n)
    arr_180 = t_90(arr_90, n)
    arr_270 = t_90(arr_180, n)

    print(f'#{a}')
    for i in range(n):
        print("".join(map(str, arr_90[i])),end=" ")
        print("".join(map(str, arr_180[i])),end=" ")
        print("".join(map(str, arr_270[i])),end="\n")