x, y = 0, 0
rx, ry = -1, -1
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num, cnt = 0, 0
s = input()

for i in s:
    if rx == 0 and ry == 0: break
    else:
        if i == 'L':
            dir_num = (dir_num + 3) % 4
            cnt += 1
        elif i == 'R':
            dir_num = (dir_num + 1) % 4
            cnt += 1
        elif i == 'F':
            x, y = x + dxs[dir_num], y + dys[dir_num]
            rx, ry = x, y
            cnt += 1
if rx == 0 and ry == 0: print(cnt)
else: print(-1)