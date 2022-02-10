dir_num = 0
x, y = 0, 0
dx, dy = [1, 0, -1, 0],[0, -1, 0, 1]

mapper = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}

n = int(input())

for _ in range(n):
  m, dist = input().split()
  dist = int(dist)
  
  dir_num = mapper[m]
  
  x, y = x + dx[dir_num] * dist, y + dy[dir_num] * dist 
  
  
print(x, y)
  