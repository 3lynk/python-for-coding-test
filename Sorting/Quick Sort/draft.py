def quick_sort(l, r):
  for rx, ry in r:
    if rx == ry:
      continue
    p = rx

    while True:
      b = -1
      for i in range(rx + 1, ry):
        if l[p] < l[i]:
          b = i
          break
  
      s = -1
      for i in range(ry - 1, rx, -1):
        if l[p] > l[i]:
          s = i
          break
  
      if b != -1 and s != -1 and b < s:
        l[b], l[s] = l[s], l[b]
      else:
        break

    if s == -1 or (s == -1 and b == -1):
      result[p] = l[p]
      quick_sort(l, [[rx + 1, ry]])
    elif b == -1 or b > s:
      result[s] = l[p]
      l[p], l[s] = l[s], l[p]

      tmp = [[rx, s]]
      if s != len(l):
        tmp.append([s + 1, ry])
      quick_sort(l, tmp)

l = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
result = [-1 for i in range(len(l))]
r = [[0, len(l)]]
cnt = 0

quick_sort(l, r)
print(result)
