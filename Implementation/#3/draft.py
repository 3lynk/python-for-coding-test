# N, M 입력
N, M = map(int, input().split())

# place 초기화
place = []

# A, B d 입력
A, B, d = map(int, input().split())
place.append([A, B])

# game_map 세팅
game_map = []
for i in range(N):
  game_map.append(list(map(int, input().split())))

# 방향, 이동 설정
toward = [3, 0, 1, 2]
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

# cnt 초기화
cnt = 0
while True:
  # 방향 설정, 다음 위치 확인
  d = toward[d]
  next_place = [A + move[d][0], B + move[d][1]]

  # 다음 위치가 1이면 cnt 증가
  if game_map[next_place[0]][next_place[1]] == 1:
    cnt += 1
  # 그렇지 않고 다음 위치가 방문했던 위치면 cnt 증가, 방문 안했었으면 그 위치로 이동, cnt 초기화
  else:
    if next_place in place:
      cnt += 1
    else:
      place.append(next_place)
      A, B = next_place[0], next_place[1]
      cnt = 0

  # 모든 방향이 방문했거나 바다이면 뒤로 이동할 준비
  if cnt == 4:
    next_place = [A + move[toward[toward[d]]][0], B + move[toward[toward[d]]][1]]
    # 뒤에 위치가 바다이면 반복문 종료, 그렇지 않으면 이동
    if game_map[next_place[0]][next_place[1]] == 1:
      break
    else:
      A, B = next_place[0], next_place[1]
      cnt = 0

# 방문한 위치(중복 없이) 개수 출력
print(len(place))
