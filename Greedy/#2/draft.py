N, M, K = map(int, input().split())

n = list(map(int, input().split()))

fb = 0
sb = 0

for i in n:
  if i >= sb:
    sb = i
  if fb <= sb:
    fb, sb = sb, fb

ans = (M // (K + 1)) * (K*fb + sb) + (M % (K + 1) * fb)
print(ans)
