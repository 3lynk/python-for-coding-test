# Binary Search(이진 탐색)

## Sequtential Search(순차 탐색)
데이터를 앞에서부터 하나씩 확인하여 탐색

### Example
```python
def sequential_search(target, data):
  for i in rane(len(data)):
    if data[i] == target:
      return i
```

### 특징
- 정렬되지 않은 리스트에서 데이터 탐색 시 사용
- 데이터가 아무리 많아도 시간만 충분하면 탐색 가능
- 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인

### 시간 복잡도
#### 최악의 경우
___O(N)___

## Binary Search(이진 탐색)
데이터의 중간점에 있는 데이터와 반복적으로 비교하여 탐색

### Example
```python
# Using Recursion
def binary_search(target, data, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if data[mid] == target:
    return mid
  
  elif data[mid] > target:
    return binary_search(target, data, start, mid - 1)
  else:
    return binary_search(target, data, mid + 1, end)
```
```python
# Using While
def binary_search(target, data, start, end):
  while start <= end:
    mid = (start + end) // 2

    if data[mid] == target:
      return mid

    if data[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
      
  return None
```

### 특징
- 데이터가 무작위일 때는 사용 불가
- 데이터가 정렬되어 있다면 빠르게 탐색 가능
- 탐색 범위를 절반씩 좁혀가며 탐색
- 탐색 범위가 큰 상황에서 유리(탐색 범위 2,000만 넘어가면 이진 탐색으로 접근 권장)

### 시간 복잡도
___O(logN)___
