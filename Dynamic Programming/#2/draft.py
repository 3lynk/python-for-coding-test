X = int(input())

d = [[1, 0]]

for i in range(2, X + 1):
  r = [d[i - 2][1] + 1]
  
  if i % 5 == 0:
    r.append(d[i // 5 - 1][1] + 1)
  if i % 3 == 0:
    r.append(d[i // 3 - 1][1] + 1)
  if i % 2 == 0:
    r.append(d[i // 2 - 1][1] + 1)

  d.append([i, min(r)])

print(d[X - 1][1])
