"""
n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

#입력
첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.

#출력
첫째 줄에 프리오더를 출력한다.
"""

import sys
sys.setrecursionlimit(100001)   #n 최대 100000이라 이래잡음
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

#처음에 인자 3개로 했다가 망함
def preorder(post_start, post_end, in_start, in_end):
    
    #구간 없으면 끝
    if in_start > in_end or post_start > post_end:
        return
    
    #postorder 맨 끝이 루트
    root = postorder[post_end]

    #inorder 루트 찾기
    mid = in_start
    while mid <= in_end and inorder[mid] != root:
        mid += 1

    #왼쪽 서브트리 크기
    left_size = mid - in_start
    
    #전위순회
    ans.append(root)

    #각 서브트리 루트노드 위치는 저래 나오던데
    preorder(post_start, post_start + left_size - 1, in_start, mid - 1)
    preorder(post_start + left_size, post_end - 1 , mid + 1, in_end)

ans = []
preorder(0, len(postorder) - 1, 0, len(inorder)-1)
print(*ans)