# binary_search
def binary_search(n) -> str:
  # set start, end
  start, end = 0, N - 1

  # loop
  while start <= end:
    mid = (start + end) // 2

    if stock[mid] == n:
      return "yes"
    
    if stock[mid] < n:
      start = mid + 1
    else:
      end = mid - 1

  return "no"

# N(1 <= N <= 1,000,000), stock, M(1 <= M <= 1,000,000), buy_list input
N = int(input())
stock = list(map(int, input().split()))
M = int(input())
buy_list = list(map(int, input().split()))

# sort stock
stock = sorted(stock)

# init result
result = []

# main
for i in buy_list:
  result.append(binary_search(i))

# print result
for i in result:
  print(i, end=" ")
