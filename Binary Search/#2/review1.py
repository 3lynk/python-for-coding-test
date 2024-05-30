# Count Sort(계수 정렬)로 해결

# set N, stock, M, buy_list
N = int(input())
stock = [0] * 1000001

for i in list(map(int, input().split())):
  stock[i] = 1

M = int(input())
buy_list = list(map(int, input().split()))

# init result
result = []

# main
for i in buy_list:
  if stock[i] == 1:
    result.append("yes")
  else:
    result.append("no")

# print result
for i in result:
  print(i, end=" ")
