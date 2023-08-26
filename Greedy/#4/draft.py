N, K = map(int, input().split())

power = 0

i = 1
while True:
  if K ** i > N:
    power = i - 1
    break
  i += 1

result = N - K ** power + power

print(result)
