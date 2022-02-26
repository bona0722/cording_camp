# 1. 예시 내의 수가 작으면 다 돌려보기 (완전탐색)
# 2. 양수인지 아닌지 판별하기
n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]


def positive_rect(x1, y1, x2, y2):
  for x in range(x1, x2+1):
    for y in range(y1, y2+1):
      if grid[x][y] <= 0:
        return False
      
  return True

ans = -1

for i in range(n):
  for j in range(m):
    for k in range(i, n):
      for l in range(j, m):
        if positive_rect(i, j, k, l):
          ans = max(ans, (k-i+1) * (l-j+1))
print(ans)