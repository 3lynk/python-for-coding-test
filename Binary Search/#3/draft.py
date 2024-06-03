# sum length
def sum_length(H) -> int:
  result = 0

  for i in reversed(length):
    if i - H <= 0:
      break
    result += (i - H)

  return result


# input N, M, length
N, M = map(int, input().split())
length = sorted(map(int, input().split()))

# init start, end, ans
start, end = 0, length[-1]
ans = []

# binary search with while
while start <= end:
  mid = (end + start) // 2

  result = sum_length(mid)

  if result == M:
    ans.append(mid)
    break
  if result < M:
    end = mid - 1
  elif result > M:
    start = mid + 1
    ans.append(mid)

# print ans
print(ans[-1])

'''memo
Input

N : len(data)
M : 손님이 요청한 값
data = [n1, n2, n3, n4, ...]


Ans

H : 절단기 높이
M >= (n1- H) + (n2 - H) + (n3 - H) + (n4 - H) + ...
max(H) = ?
'''
