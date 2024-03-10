def count_sort(data):
  max_data = max(data)
  min_data = min(data)

  tmp = [0 for _ in range(max_data - min_data + 1)]

  for i in data:
    tmp[i - min_data] += 1

  print(tmp)

  for i in range(len(tmp)):
    for k in range(tmp[i]):
      print(f"{i + min_data} ", end="")

data = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count_sort(data)
