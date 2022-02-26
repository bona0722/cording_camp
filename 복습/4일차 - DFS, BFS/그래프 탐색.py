n, m = tuple(map(int, input().split()))

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
cnt = 0

def dfs(vertex): #재귀적으로 탐색해주는 코드
    global cnt
    for curr_v in range(1, n+1):
    #1부터 n번까지 순회하는 for문
        if graph[vertex][curr_v] and not visited[curr_v]: #현재 위치에서 연결되어 있는 것들을 모두 탐색. 1인지를 봐야함
      # == 1을 안 쓴 이유? 정수값에 대해서 아무것도 안 적으면 != 0과 의미가 같다.
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)
      
      
# a = 3일 때, if a: <=> if a != 0
# if a == 0: <=> if not a:

# a = True 일 때, if a: <=> if a == True
# if not a: <=> if a == False: 

for _ in range(m):
  x, y = tuple(map(int, input().split()))
  graph[x][y] = 1
  graph[y][x] = 1
  
root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
print(cnt)
