n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_gold = 0


def get_num_of_gold(row_s, row_e, col_s, col_e):
    cnt = 0
    for i in range(row_s, row_e + 1):
        for j in range(col_s, col_e + 1):
          if grid[i][j] == 1:
            cnt += 1
    return cnt


for row in range(n):
  for col in range(n):
    if row + 2 >= n or col + 2 >= n: 
      continue
    
    goldCnt = get_num_of_gold(row, row+2, col, col+2)
    max_gold = max(max_gold, goldCnt)
    
print(max_gold)