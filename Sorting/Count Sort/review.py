def count_sort(data):
  count = [0] * (max(data) + 1)

  for i in range(len(data)):
    count[data[i]] += 1

  for i in range(len(count)):
    for k in range(count[i]):
      print(i, end=" ")

data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count_sort(data)
