#   2
# 1   0
#   3
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = tuple(map(int, input().split()))
arr = [[0] * n for _ in range(n)]
ans =[]
def in_range(x, y):
  return 0 <= x and x < n and 0 <= y and y < n
  
def oneCnt(x, y):
  cnt = 0 #1count  
  for dx, dy in zip(dxs, dys):
    nx, ny = x + dx , y + dy
    if in_range(nx, ny) and arr[nx][ny] == 1: cnt += 1
  
  return cnt
    
for _ in range(m):
    r, c = list(map(int, input().split()))
    arr[r-1][c-1] = 1
    if oneCnt(r-1, c-1) >= 3: ans.append(1)
    else: ans.append(0)

for i in ans:
  print(i)
      

  

    
  