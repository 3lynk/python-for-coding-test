global stack

def ice(visited, ice_frame, pos):
  visited[pos[0]][pos[1]] = True
  stack.append(pos)

  cnt = 0
  for i in urdl:
    x, y = pos[0] + i[0], pos[1] + i[1]

    if x < 0 or y < 0 or x > N - 1 or y > M - 1:
      continue

    if visited[x][y] == False and ice_frame[x][y] == "0":
      cnt += 1

      visited = ice(visited, ice_frame, [x, y])

  if cnt == 0:
    stack.pop()
      
  return visited

# N, M 입력 받기
N, M = map(int, input().split())

# ice_frame 입력 받기
ice_frame = []
for _ in range(N):
  ice_frame.append(list(str(input())))

# visited 초기화
visited = [[False for _ in range(M)] for _ in range(N)]

# 방향 좌표
urdl = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# stack, sol 초기화
stack = []
sol = 0

for i in range(N):
  for k in range(M):
    if ice_frame[i][k] == "0" and visited[i][k] == False:
      visited = ice(visited, ice_frame, [i, k])
      sol += 1

print(sol)
