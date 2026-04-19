# DFS / 백트래킹

---

## 1949 - 등산로 조성

### 1. 핵심 아이디어
- N×N 지도에서 **가장 높은 봉우리**에서 출발
- **높은 → 낮은** 방향으로만 이동 (상하좌우)
- 딱 **한 곳**을 최대 K만큼 깎을 수 있음 → DFS 파라미터로 깎기 여부 전달
- 가장 긴 등산로 길이 출력

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

def dfs(x, y, length, cut):
    global ans
    ans = max(ans, length)

    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            # 현재보다 낮으면 그냥 이동
            if board[nx][ny] < board[x][y]:
                dfs(nx, ny, length + 1, cut)
            # 깎지 않았고, 깎으면 현재보다 낮아지는 경우
            elif not cut and board[nx][ny] - K < board[x][y]:
                # 깎아서 현재 높이보다 1 낮게 만들어 이동
                original = board[nx][ny]
                board[nx][ny] = board[x][y] - 1
                dfs(nx, ny, length + 1, True)
                board[nx][ny] = original  # 복원

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_h = max(map(max, board))
    ans = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == max_h:
                dfs(i, j, 1, False)

    print(f'#{tc} {ans}')
```

---

## 2105 - 디저트 카페

### 1. 핵심 아이디어
- N×N 지도에서 **대각선 방향**으로 이동하는 사각형 경로 탐색
- 시작점 기준으로 우하→좌하→좌상→우상 순으로 DFS
- 경로 위 카페 번호 **중복 없이** 방문해야 함
- 시작점으로 돌아왔을 때 최대 방문 수 갱신

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

# 대각선 방향: 우하, 좌하, 좌상, 우상
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def dfs(x, y, direction, count, sx, sy):
    global ans
    for d in range(direction, 4):
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < N and 0 <= ny < N):
            break
        # 마지막 방향에서 시작점으로 돌아온 경우
        if d == 3 and nx == sx and ny == sy:
            ans = max(ans, count)
            return
        # 중복 방문 체크
        if visited[board[nx][ny]]:
            break
        visited[board[nx][ny]] = True
        dfs(nx, ny, d, count + 1, sx, sy)
        visited[board[nx][ny]] = False
        break  # 한 방향으로만 직진

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * 101
    ans = -1

    for i in range(N):
        for j in range(N):
            visited[board[i][j]] = True
            dfs(i, j, 0, 1, i, j)
            visited[board[i][j]] = False

    print(f'#{tc} {ans}')
```

---

## 2112 - 보호 필름

### 1. 핵심 아이디어
- D×W 필름에서 약품을 **최소 몇 번** 투입해야 성능 기준 K를 만족하는지
- 각 행에 A 투입, B 투입, 그대로 중 선택 → DFS + 백트래킹
- 모든 열에서 세로 방향으로 같은 값이 K개 연속인지 확인
- 현재 깊이가 이미 구한 최솟값 이상이면 가지치기

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

def check():
    for j in range(W):
        cnt = 1
        for i in range(1, D):
            if film[i][j] == film[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                break
        else:
            # 이 열은 K개 연속 없음
            return False
    return True

def dfs(row, count):
    global ans
    if count >= ans:
        return
    if check():
        ans = min(ans, count)
        return
    if row == D:
        return

    original = film[row][:]

    # 그대로
    dfs(row + 1, count)

    # A로 덮기
    film[row] = [0] * W
    dfs(row + 1, count + 1)

    # B로 덮기
    film[row] = [1] * W
    dfs(row + 1, count + 1)

    film[row] = original  # 복원

T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    ans = D  # 최악의 경우 모든 행 투입

    if check():
        ans = 0
    else:
        dfs(0, 0)

    print(f'#{tc} {ans}')
```

---

## 4008 - 숫자 만들기

### 1. 핵심 아이디어
- N개의 숫자와 연산자(+, -, ×, ÷) 개수가 주어짐
- 연산자 순서를 바꿔가며 순열로 모든 경우 탐색
- 최댓값 - 최솟값 출력
- 연산자 개수로 재귀 → 순열 DFS

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

def dfs(idx, value):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, value)
        min_val = min(min_val, value)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            num = numbers[idx]
            if i == 0:
                dfs(idx + 1, value + num)
            elif i == 1:
                dfs(idx + 1, value - num)
            elif i == 2:
                dfs(idx + 1, value * num)
            else:
                dfs(idx + 1, int(value / num))  # 음수 나눗셈 주의
            ops[i] += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ops = list(map(int, input().split()))  # +, -, *, /
    numbers = list(map(int, input().split()))

    max_val = -float('inf')
    min_val = float('inf')
    dfs(1, numbers[0])

    print(f'#{tc} {max_val - min_val}')
```

---

## 4012 - 요리사

### 1. 핵심 아이디어
- N개의 재료를 절반씩 나눠 A 음식과 B 음식 만들기
- 재료 배분의 모든 경우를 DFS(부분집합)로 탐색
- A 음식, B 음식 각각의 맛(재료 조합 시너지 합) 계산 후 차이 최솟값 출력
- N은 최대 16 → 조합의 수는 C(16,8) = 12870으로 완전탐색 가능

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

def calc_taste(group):
    total = 0
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            total += synergy[group[i]][group[j]]
            total += synergy[group[j]][group[i]]
    return total

def dfs(idx, group_a):
    global ans
    if len(group_a) == N // 2:
        group_b = [i for i in range(N) if i not in group_a]
        diff = abs(calc_taste(group_a) - calc_taste(group_b))
        ans = min(ans, diff)
        return
    if idx == N:
        return
    # 남은 재료로 절반 채울 수 있을 때만 탐색
    if N - idx < N // 2 - len(group_a):
        return

    group_a.append(idx)
    dfs(idx + 1, group_a)
    group_a.pop()
    dfs(idx + 1, group_a)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    dfs(0, [])
    print(f'#{tc} {ans}')
```

---

## 5656 - 벽돌 깨기

### 1. 핵심 아이디어
- W개의 열 중 N번 구슬을 던질 열을 선택 (중복 허용)
- 구슬이 내려가며 맞은 벽돌 연쇄 폭발 (BFS로 처리)
- N번 구슬 선택 경우의 수는 W^N → W≤12, N≤4이므로 완전탐색 가능
- 매 시뮬레이션 후 보드 상태를 복원하여 다음 경우 탐색

### 2. 파이썬 코드

```python
import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

def drop(board, col):
    # 구슬 떨어뜨리기
    for r in range(H):
        if board[r][col] > 0:
            val = board[r][col]
            board[r][col] = 0
            # BFS로 연쇄 폭발
            q = deque()
            q.append((r, col, val))
            while q:
                cx, cy, cv = q.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    for d in range(1, cv):
                        nx, ny = cx + dx * d, cy + dy * d
                        if 0 <= nx < H and 0 <= ny < W and board[nx][ny] > 0:
                            q.append((nx, ny, board[nx][ny]))
                            board[nx][ny] = 0
            break

    # 벽돌 아래로 내리기
    for c in range(W):
        col_vals = [board[r][c] for r in range(H) if board[r][c] > 0]
        for r in range(H):
            if H - len(col_vals) <= r:
                board[r][c] = col_vals[r - (H - len(col_vals))]
            else:
                board[r][c] = 0

def dfs(board, count):
    global ans
    if count == N:
        remaining = sum(1 for r in range(H) for c in range(W) if board[r][c] > 0)
        ans = min(ans, remaining)
        return
    for c in range(W):
        new_board = deepcopy(board)
        drop(new_board, c)
        dfs(new_board, count + 1)

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    dfs(board, 0)
    print(f'#{tc} {ans}')
```
