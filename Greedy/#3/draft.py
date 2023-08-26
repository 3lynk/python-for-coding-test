N, M = map(int, input().split())

card = []

for i in range(N):
  card.append(list(map(int, input().split())))

result = 0

for i in card:
  i.sort()

  if result < i[0]:
    result = i[0]

print(result)
