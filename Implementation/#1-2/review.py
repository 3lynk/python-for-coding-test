N = int(input())

ans = 0

for i in range(0, N + 1):
  for k in range(0, 60):
    for l in range(0, 60):
      # 3이 포함하는지 판별하는 과정이 비효율적임
      '''if l // 10 == 3 or l % 10 == 3:
        ans += 1
      elif k // 10 == 3 or k % 10 == 3:
        ans += 1
      elif i // 10 == 3 or i % 10 == 3:
        ans += 1'''
      if '3' in str(i) + str(k) + str(l):
        ans += 1

print(ans)
