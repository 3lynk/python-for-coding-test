from collections import deque

def maze_dfs(x, y):
  queue = deque()
  queue.append([x, y])

  sol = 1

  while queue:
    x, y = map(int, queue.popleft())
    
    for p1, p2 in pos:
      px, py = x + p1, y + p2

      if px < 0 or py < 0 or px >= N or py >= M:
        continue

      if maze[px][py] == 1:
        sol += 1
        maze[px][py] = maze[x][y] + 1
        queue.append([px, py])

    if x == N - 1 and y == M - 1:
      break

  return maze[N - 1][M - 1]

# N, M 입력 받기
N, M = map(int, input().split())

# maze 입력 받기
maze = []

for _ in range(N):
  maze.append(list(map(int, input())))

# pos 초기화
pos = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# main
print(maze_dfs(0, 0))
