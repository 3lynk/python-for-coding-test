def ice(x, y):
  ice_frame[x][y] = 1

  for p1, p2 in pos:
    px, py = x + p1, y + p2

    if px < 0 or py < 0 or px >= N or py >= M:
      continue

    if ice_frame[px][py] == 0:
      ice(px, py)
  return 0

# N, M 입력 받기
N, M = map(int, input().split())

# ice_frame 입력 받기
ice_frame = []

for _ in range(N):
  ice_frame.append(list(map(int, input())))

# sol 초기화
sol = 0

# pos 초기화
pos = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# main
for i in range(N):
  for k in range(M):
    if ice_frame[i][k] == 0:
      ice(i, k)
      sol += 1

print(sol)

```
dfs 구현시 stack을 사용하려는 거에 중점을 맞추다 보니 코드가 복잡해지고 visited라는 불필요한 변수도 생기게 됨
리스트 요소가 0과 1 두 가지 밖에 없으므로 방문처리를 간단하게 처리함으로써 코드를 전반적으로 간단화 시킴
```
