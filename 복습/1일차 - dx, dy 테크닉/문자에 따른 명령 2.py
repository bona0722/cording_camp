#    0
#  3   1
#    2

s = input()
dir_num = 0
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


for i in s:
  if i == 'L': #반시계 방향
    dir_num = (dir_num + 3) % 4
  elif i == 'R': #시계 방향
    dir_num = (dir_num + 1) % 4
  else:
    x, y = x + dx[dir_num], y + dy[dir_num]
    
print(x, y)