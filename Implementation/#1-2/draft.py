N = int(input())

ans = 0

for i in range(0, N + 1):
  for k in range(0, 60):
    for l in range(0, 60):
      if l // 10 == 3 or l % 10 == 3:
        ans += 1
      elif k // 10 == 3 or k % 10 == 3:
        ans += 1
      elif i // 10 == 3 or i % 10 == 3:
        ans += 1

print(ans)
