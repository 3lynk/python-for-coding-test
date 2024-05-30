# Set(집합)으로 해결

# set N, stock, M, buy_list input
N = int(input())
stock = list(map(int, input().split()))
M = int(input())
buy_list = list(map(int, input().split()))

# main
for i in buy_list:
  if i in stock:
    print("yes", end=" ")
  else:
    print("no", end=" ")
