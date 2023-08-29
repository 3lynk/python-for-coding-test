xy = input()

x = int(ord(xy[:1]) - ord("a"))
y = int(xy[1:]) - 1

ans = 8

if x + 1 > 7 or x - 1 < 0:
  ans -= 4

  if y + 1 > 7 or y - 1 < 0:
    ans -= 2
  elif y + 2 > 7 or y - 2 < 0:
    ans -= 1

elif x + 2 > 7 or x - 2 < 0:
  ans -= 2

  if y + 1 > 7 or y - 1 < 0:
    ans -= 3
  elif y - 2 > 7 or y - 2 < 0:
    ans -= 2

print(ans)
