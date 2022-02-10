# 1개의 구슬이 n*n 격자 안에 놓여져 있고, 격자는 벽으로 둘러쌓여 있습니다. 이 구슬은 방향을 갖고 있고, 해당 방향으로 1초에 한칸 씩 움직입니다.
# 구슬이 벽에 부딪히면 움직이는 방향이 반대로 뒤집혀 동일한 속도로 움직이는 것을 반복합니다. 이때 방향을 바꾸는 데에는 시간이 1만큼 소요됩니다.
# 처음 주어진 그림을 예로 4초 뒤까지의 모습을 순서대로 그려보면 다음과 같습니다.
# 구슬의 처음 위치와 초기 방향이 주어졌을 때, t초가 지난 이후에 해당 구슬의 위치를 구하는 프로그램을 작성해보세요.

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

n, t = tuple(map(int, input().split()))
r, c, d = input().split()
x, y = int(r), int(c)

mapper = {
    "U": 2,
    "D": 1,
    "R": 0,
    "L": 3
}

dir_num = mapper[d]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n
#0이 되면 더이상 갈 데가 없음! 방향을 바꿔주기 위한 range이니 1보다 크거나 같아야하고 n보다 작거나 같아야 함



for _ in range(t):
  
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    if not in_range(nx, ny):
        dir_num = 3 - dir_num
    else: #x와 y를 다음에 나타낼 수인 nx와 ny로 나타낸다.
        x, y = nx, ny

print(x, y)

#안 풀리던 이유: 33줄에 nx, ny를 정의해주어서 안 되었었음