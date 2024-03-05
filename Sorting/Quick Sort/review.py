def quick_sort(arr):
  # arr의 길이가 1보다 작다는 것은 더 이상 비교할 값이 없으므로 그대로 반환
  if len(arr) <= 1:
    return arr

  # pivot 설정
  p = arr[0]
  # 탐색을 진행하는 부분은 피봇을 제외한 부분이므로, 피봇을 제외한 리스트 생성
  tail = arr[1:]

  # 피봇을 제외한 부분 내에서 큰 수, 작은 수 교환 후 피봇 위치 조정을 하면, 피봇을 기준으로 피봇의 왼쪽에는 피봇보다 작은 수, 오른쪽에는 피봇보다 큰 수가 들어가므로
  # 간단하게 피봇보다 작은 수의 리스트와 피봇보다 큰 수의 리스트로 분할
  left = [x for x in tail if x <= p]
  right = [x for x in tail if x > p]

  # 앞서 퀵 소트의 특성상 피봇을 기준으로 왼쪽에 작은 수, 오른쪽에 큰 수 형태의 리스트 리턴
  return quick_sort(left) + [p] + quick_sort(right)

l = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

print(quick_sort(l))
