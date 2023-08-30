def d_count(d):
  if d == 0:
    return 3
  else:
    return d - 1

def move(A, B, d):
  if d == 0:
    return [A, B - 1]
  elif d == 1:
    return [A + 1, B]
  elif d == 2:
    return [A, B + 1]
  else:
    return [A - 1, B]

N, M = map(int, input().split())

place = []
ans = 0

A, B, d = map(int, input().split())
place.append([A, B])

game_map = []
for i in range(N):
  game_map.append(input().split())

cnt = 0
while True:
  d = d_count(d)
  next_place = move(A, B, d)

  if next_place[0] < 0 or next_place[1] < 0 or next_place[0] > M or next_place[0] > N:
    cnt += 1
  elif game_map[next_place[1]][next_place[0]] == "1":
    cnt += 1
  elif next_place in place:
    cnt += 1
  else:
    A, B = next_place[0], next_place[1]
    place.append([A, B])
    cnt = 0

  if cnt == 4:
    tmp_d = d - 2
    if tmp_d < 0:
      tmp_d *= -1
      
    if game_map[move(A, B, tmp_d)[1]][move(A, B, tmp_d)[0]] == "1":
      break
    else:
      A, B = move(A, B, tmp_d)[0], move(A, B, tmp_d)[1]

print(len(place))
