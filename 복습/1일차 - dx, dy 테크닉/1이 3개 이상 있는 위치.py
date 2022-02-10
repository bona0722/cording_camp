dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
nx, ny = 0, 0
cnt, ans = 0, 0

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
  return 0 <= x and x < n and 0 <= y and y < n


def count(x, y):
  cnt = 0 
  for dx, dy in zip(dxs, dys):
    nx, ny = x + dx, y + dy
    if in_range(nx, ny) and arr[nx][ny] == 1:
      cnt += 1
      
  return cnt

for i in range(len(arr)):
  for j in range(len(arr)):    
    cnt = count(i, j)
    if cnt >= 3: ans+=1
  
print(ans)