# 암시적 그래프 : 현실 세계에서 그래프 구조가 아닌데 그래프로 표현하면 쉽게 해결될 수 있는 문제
from collections import deque

def isValid(r, c):
    return 0 <= r < row_len and 0 <= c < col_len and grid[r][c] == 1

def dfs(r, c):
    visited[r][c] = True
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if isValid(next_r, next_c):
            if not visited[next_r][next_c]:
                dfs(next_r, next_c)

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            next_r = cur_r + dr[i]
            next_c = cur_c + dc[i]
            if isValid(next_r, next_c):
                if not visited[next_r][next_c]:
                    queue.append((next_r, next_c))
                    visited[next_r][next_c] = True

grid = [[1, 1, 1, 1],
        [0, 1, 0, 1],
        [0, 1, 0, 1],
        [1, 0, 1, 1]]

row_len, col_len = len(grid), len(grid[0])
visited = [[False] * col_len for _ in range(row_len)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# dfs(0, 0)
bfs(0, 0)