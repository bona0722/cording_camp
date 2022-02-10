dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]
tim, cnt = 0, 0
x, y = 0, 0
rx, ry = -1, -1 #result x, y
mapper = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3
}

n = int(input())


def checkLoc(x, y):
    if x == 0 and y == 0:
        return True
    else:
        return False


for _ in range(n):
    dirc, dist = input().split()
    dist = int(dist)
    dir_num = mapper[dirc]

    for i in range(dist):
      nx, ny = x + dxs[dir_num], y + dys[dir_num]
      
      if not checkLoc(nx, ny):
        x, y = nx, ny
        cnt += 1
      else: 
        rx, ry = nx, ny
        tim += cnt + 1
        brk = True
        break
    if checkLoc(rx, ry):
      break

if rx == 0 and ry == 0:
  print(tim)
else: print(-1)

