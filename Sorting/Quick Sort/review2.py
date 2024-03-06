def quick_sort(l, r):
  for rx, ry in r:
    if rx >= ry:
      continue
    pivot = rx

    left, right = rx + 1, ry

    while left <= right:
      while left <= ry and l[left] <= l[pivot]:
        left += 1
      while right > rx and l[right] >= l[pivot]:
        right -= 1

      if left > right:
        l[right], l[pivot] = l[pivot], l[right]
      else:
        l[right], l[left] = l[left], l[right]

    quick_sort(l, [[rx, right - 1], [right + 1, ry]])

l = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

quick_sort(l, [[0, len(l) - 1]])

# review.py의 quick sort는 구현하기 간단하긴 하지만 실제 비교 연산 횟수가 증가하여 다소 비효율적
# review2.py는 draft에서 드러난 큰 값과 작은 값이 엇갈렸을 때 비교 중단하는 quick sort의 특징을 살려 다듬어 낸 코드
