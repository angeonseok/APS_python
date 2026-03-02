"""
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
예를 들어 위와 같은 이진 트리가 입력되면,
전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

#입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

#출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
"""

#부모 > 왼 > 오
def preorder(v):
    if v != ".":
        print(v, end="")
        preorder(tree[v][0])
        preorder(tree[v][1])

#왼 > 부모 > 오
def inorder(v):
    if v != ".":
        inorder(tree[v][0])
        print(v, end = "")
        inorder(tree[v][1])

#왼 > 오 > 부모
def postorder(v):
    if v != ".":
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end = "")

import sys
input = sys.stdin.readline 

n = int(input())

#부모를 키 값으로, 자식을 벨류값으로
tree = {}
for _ in range(n):
    p, l_c, r_c = map(str, input().split())
    tree[p] = l_c, r_c

preorder("A")
print()

inorder("A")
print()

postorder("A")
print()