N = int(input())
cmd = list(map(str, input().split()))

h, v = 1, 1

for i in cmd:
  if i == "R":
    if h + 1 > N:
      pass
    else:
      h += 1
  elif i == "L":
    if h - 1 < 1:
      pass
    else:
      h -= 1
  elif i == "U":
    if v - 1 < 1:
      pass
    else:
      v -= 1
  elif i == "D":
    if v + 1 > N:
      pass
    else:
      v += 1

print(v, h)
