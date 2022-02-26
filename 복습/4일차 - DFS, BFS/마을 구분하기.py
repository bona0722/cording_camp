n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
pNum = []


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    if not in_range(x, y):
        return False
    elif visited[x][y] or grid[x][y] == 0:
        return False
    return True


def dfs(x, y):
    global cnt
    dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if can_go(nx, ny):
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True
            cnt = 1
            dfs(i, j)
            pNum.append(cnt)

pNum.sort()

for i in range(len(pNum)):
    print(pNum[i])