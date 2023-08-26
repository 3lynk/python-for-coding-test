N, M, K = map(int, input().split())

n = list(map(int, input().split()))

# 가장 큰 수와 그 다음으로 큰 수를 구하는 방법이 비효율적임

n.sort()
fb = n[-1]
sb = n[-2]

'''
fb = 0
sb = 0


for i in n:
  if i >= sb:
    sb = i
  if fb <= sb:
    fb, sb = sb, fb
'''

ans = (M // (K + 1)) * (K*fb + sb) + (M % (K + 1) * fb)
print(ans)
