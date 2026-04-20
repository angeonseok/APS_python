# BFS / 격자 탐색 시뮬레이션

---

## 1953 - 탈주범 검거

### 1. 핵심 아이디어
- N×M 지도에서 탈주범이 출발점에서 L시간 내 이동 가능한 칸 수 구하기
- 터널 타입(1~7)에 따라 이동 가능한 방향이 다름
- BFS로 L 거리 이내 도달 가능한 칸 탐색
- 양쪽 터널이 서로 연결되는지 방향 체크 필요

### 2. 파이썬 코드

```python
import sys
from collections import deque
input = sys.stdin.readline

# 상 하 좌 우 순서
# 터널 타입별 이동 가능한 방향 (상, 하, 좌, 우) = (0, 1, 2, 3)
tunnel = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
}
# 반대 방향
opposite = {0: 1, 1: 0, 2: 3, 3: 2}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    q = deque()
    q.append((R, C, 1))
    ans = 1

    while q:
        x, y, dist = q.popleft()
        if dist == L:
            continue
        cur_type = board[x][y]
        for d in tunnel[cur_type]:
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                next_type = board[nx][ny]
                # 다음 칸 터널이 반대 방향을 가지고 있어야 연결 가능
                if next_type > 0 and opposite[d] in tunnel[next_type]:
                    visited[nx][ny] = True
                    ans += 1
                    q.append((nx, ny, dist + 1))

    print(f'#{tc} {ans}')
```

---

## 2117 - 홈 방범 서비스

### 1. 핵심 아이디어
- 마름모(다이아몬드) 형태로 서비스 범위를 확장하며 최대 이익 계산
- 서비스 크기 K일 때 마름모 범위: |dx| + |dy| < K
- 모든 집에 대해 마름모 범위를 완전탐색하면 TLE → 집을 중심으로 역발상
- 각 크기 K에 대해 포함된 집 수를 세고, 비용 대비 이익 계산

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 모든 점을 중심으로 시도
    for cx in range(N):
        for cy in range(N):
            houses = 0
            # K = 1부터 2N-1까지
            for K in range(1, 2 * N):
                # K가 늘어날 때 새로 포함되는 테두리 칸 계산
                # 마름모 테두리: |dx| + |dy| == K - 1
                for dx in range(-K + 1, K):
                    dy_val = K - 1 - abs(dx)
                    for dy in [dy_val, -dy_val]:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            houses += board[nx][ny]
                        if dy_val == 0:
                            break  # 중복 방지

                cost = K * K + (K - 1) * (K - 1)
                profit = houses * M - cost
                if profit >= 0:
                    ans = max(ans, houses)

    print(f'#{tc} {ans}')
```

---

## 2382 - 미생물 격리

### 1. 핵심 아이디어
- 매 시간마다 미생물 군집이 방향대로 이동
- 가장자리 도달 시 방향 반전, 크기 절반으로 감소
- 같은 칸에 여러 군집이 모이면 가장 큰 군집 방향으로 합체
- 딕셔너리/리스트로 위치별 군집 관리

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

# 방향: 1=상, 2=하, 3=좌, 4=우
dx = {1: -1, 2: 1, 3: 0, 4: 0}
dy = {1: 0, 2: 0, 3: -1, 4: 1}
reverse = {1: 2, 2: 1, 3: 4, 4: 3}

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    groups = []
    for _ in range(K):
        r, c, num, d = map(int, input().split())
        groups.append([r, c, num, d])

    for _ in range(M):
        # 이동
        for g in groups:
            g[0] += dx[g[3]]
            g[1] += dy[g[3]]
            # 가장자리 처리
            if g[0] == 0 or g[0] == N - 1 or g[1] == 0 or g[1] == N - 1:
                g[3] = reverse[g[3]]
                g[2] //= 2

        # 같은 위치 합체
        pos = {}
        for g in groups:
            if g[2] == 0:
                continue
            key = (g[0], g[1])
            if key not in pos:
                pos[key] = g
            else:
                # 더 큰 군집 방향 채택
                if g[2] > pos[key][2]:
                    pos[key][3] = g[3]
                pos[key][2] += g[2]

        groups = list(pos.values())

    total = sum(g[2] for g in groups)
    print(f'#{tc} {total}')
```

---

## 5653 - 줄기세포 배양

### 1. 핵심 아이디어
- 줄기세포가 생명력 수치만큼 비활성 → 활성 → 사멸 사이클
- 활성 상태일 때 상하좌우 빈 칸으로 번식
- 같은 칸에 여러 세포가 번식하면 생명력 높은 것만 살아남음
- BFS + 시간 시뮬레이션, 지도 좌표 이동(음수 방지용 offset)

### 2. 파이썬 코드

```python
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    OFFSET = 300
    SIZE = 700

    # cell[x][y] = (생명력, 활성화_시작_시간)
    cell = [[None] * SIZE for _ in range(SIZE)]
    q = deque()

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                v = board[i][j]
                x, y = i + OFFSET, j + OFFSET
                cell[x][y] = (v, v)  # 생명력, 활성 시작 시각
                q.append((x, y, v, v))  # x, y, 생명력, 활성시작

    for t in range(1, K + 1):
        next_q = deque()
        size = len(q)
        for _ in range(size):
            x, y, v, active_t = q.popleft()
            # 활성 상태 체크
            if t < active_t:
                next_q.append((x, y, v, active_t))
                continue
            if t >= active_t + v:
                continue  # 사멸
            # 활성 상태 → 번식
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if cell[nx][ny] is None:
                    cell[nx][ny] = (v, t + v)
                    next_q.append((nx, ny, v, t + v))
                elif cell[nx][ny][0] < v:
                    cell[nx][ny] = (v, t + v)
            next_q.append((x, y, v, active_t))
        q = next_q

    ans = sum(1 for i in range(SIZE) for j in range(SIZE) if cell[i][j] is not None and cell[i][j][1] <= K < cell[i][j][1] + cell[i][j][0])
    # 실제로는 K시점에 활성/비활성 세포 모두 카운트
    ans2 = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if cell[i][j]:
                v, active_t = cell[i][j]
                born_t = active_t - v  # 비활성 시작 = 태어난 시각
                if born_t <= K < active_t + v:
                    ans2 += 1

    print(f'#{tc} {ans2}')
```

---

## 5648 - 원자 소멸 시뮬레이션

### 1. 핵심 아이디어
- 원자들이 방향대로 이동하다가 같은 위치에서 만나면 소멸 + 에너지 합산
- 0.5 단위 이동 → 좌표를 2배로 확장해서 정수로 처리
- 매 단계 이동 후 같은 위치 원자 체크
- 딕셔너리로 위치별 원자 관리

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

# 방향: 0=상, 1=하, 2=좌, 3=우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = []
    for _ in range(N):
        x, y, d, e = map(int, input().split())
        atoms.append([x * 2, y * 2, d, e])  # 좌표 2배

    ans = 0
    MAX = 4001 * 2

    for _ in range(MAX):
        # 이동
        for a in atoms:
            a[0] += dx[a[2]]
            a[1] += dy[a[2]]

        # 같은 위치 체크
        pos = {}
        for i, a in enumerate(atoms):
            key = (a[0], a[1])
            if key not in pos:
                pos[key] = []
            pos[key].append(i)

        dead = set()
        for key, idxs in pos.items():
            if len(idxs) >= 2:
                for i in idxs:
                    ans += atoms[i][3]
                    dead.add(i)

        atoms = [a for i, a in enumerate(atoms) if i not in dead]

        # 범위 벗어나면 제거
        atoms = [a for a in atoms if -MAX <= a[0] <= MAX and -MAX <= a[1] <= MAX]

        if not atoms:
            break

    print(f'#{tc} {ans}')
```

---

## 5650 - 핀볼 게임

### 1. 핵심 아이디어
- N×N 지도에서 핀볼이 튕기며 이동, 출발점으로 돌아오는 최대 점수 계산
- 블랙홀(0)에 빠지면 종료, 벽에 닿으면 반사
- 각 빈 칸에서 출발해 시뮬레이션 → O(N³) 허용
- 장애물 번호별 반사 방향 규칙 적용

### 2. 파이썬 코드

```python
import sys
input = sys.stdin.readline

# 방향: 0=상, 1=하, 2=좌, 3=우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 장애물별 반사: reflect[장애물번호][입력방향] = 출력방향
reflect = {
    1: {0: 3, 1: 2, 2: 1, 3: 0},  # ↑→, ↓←, ←↓, →↑
    2: {0: 2, 1: 3, 2: 0, 3: 1},
    3: {0: 1, 2: 3, 1: 0, 3: 2},
    4: {0: 0, 1: 1, 2: 3, 3: 2},
    5: {0: 1, 1: 0, 2: 3, 3: 2},  # 상하 반전, 좌우 반전
}

def simulate(board, N, sx, sy, sd):
    x, y, d = sx, sy, sd
    score = 0
    while True:
        x += dx[d]
        y += dy[d]
        # 벽 처리
        hit_wall = False
        if x < 0 or x >= N:
            d = 1 - d if d <= 1 else d  # 상하 반전
            d = {0:1, 1:0, 2:2, 3:3}[d]
            x = max(0, min(N-1, x))
            hit_wall = True
        if y < 0 or y >= N:
            d = {2:3, 3:2, 0:0, 1:1}[d]
            y = max(0, min(N-1, y))
            hit_wall = True
        if hit_wall:
            score += 1
        cell = board[x][y]
        if cell == -1:  # 블랙홀
            return 0
        if cell > 0:    # 장애물
            d = reflect[cell][d]
            score += 1
        if x == sx and y == sy:
            return score

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for d in range(4):
                    ans = max(ans, simulate(board, N, i, j, d))
    print(f'#{tc} {ans}')
```
