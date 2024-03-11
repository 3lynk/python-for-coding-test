# Sorting(정렬)
데이터를 특정한 기준에 따라서 순서대로 나열하는 것

### Stable Sort
중복된 데이터를 원래 순서와 동일하게 정렬
### Unstable Sort
중복된 데이터가 원래 순서와 다르게 정렬될 가능성 존재
### In-place sorting(제자리 정렬)
리스트 안에서 교환하는 방식 => 다른 메모리 사용 X


## Selection Sort(선택 정렬)
1. 데이터 중에서 최소값 데이터 탐색
2. 최소값의 데이터가 가장 앞의 데이터 보다 작다면 Swap
3. 가장 앞의 데이터를 제외하고 반복

### Example
```python
for i in range(len(data)):
  min = i

  for k in range(i + 1, len(data)):
    if data[k] < data[min]:
      min = k

  data[i], data[min] = data[min], data[i]
```

### 시간 복잡도
(N - 1) + (N - 2) + ... + 1  
=> N * (N - 1) / 2  
___O(N^2)___

### 장점
- 구현이 간단
- In-place sorting
- Bubble Sort에 비해 실제 Swap 횟수 ↓ => Bubble Sort 보다는 조금 더 빠름

### 단점
- 최선의 경우에도 O(N^2) => 비효율적
- Unstable Sort


## Insert Sort(삽입 정렬)
1. 두 번째 데이터부터 탐색
2. 현재 데이터 인덱스 이전의 정렬된 데이터 안에서 현재 데이터가 들어갈 자리에 데이터 삽입

### Example
```python
for i in range(1, len(data)):
  for k in range(i, 0, -1):
    if data[k] < data[k - 1]:
      data[k], data[k - 1] = data[k - 1], data[k]
    else:
      break
```

### 시간 복잡도
#### 최선의 경우
1 + 1 + ... + 1 + 1  
=> N - 1  
___O(N)___
#### 최악의 경우
1 + 2 + ... + (N - 2) + (N - 1)  
=> N * (N - 1) / 2  
___O(N^2)___

### 장점
- 구현이 간단
- 데이터가 거의 정렬된 상태라면 매우 빠르게 동작
- 시간 복잡도가 O(N^2)인 Bubble Sort, Selection Sort에 비해 속도 ↑
- Stable Sort
- In-place sorting

### 단점
- 평균과 최악의 경우 O(N^2) => 비효율적


## Quick Sort(퀵 정렬)
1. 피봇을 설정
2. 피봇을 기준으로 작은 값은 왼쪽, 큰 값은 왼쪽에 위치
3. 피봇을 제외한 왼쪽, 오른쪽 리스트에서 반복

### 특징
__Hoare Partition__   
- 양쪽 끝에서 pivot보다 큰 값과 작은 값 탐색  
- Lomuto는 모든 인자가 같거나 정렬된 리스트에 대하여 swap을 발생  
=> Hoare Partition이 평균적으로 swap 3배 적게 발생 => 더 효율적

__Lomuto Partition__  
- 한쪽 끝에서 두 개의 변수가 함께 증가하며 탐색
  
__Medium Pivot__
- Pivot 값을 어떻게 설정하느냐에 따라 효율성 변동
- 값 중에서 중간 값을 피봇으로 설정하는 것이 가장 효율적
- 리스트의 첫번째 값, 중간번째 값, 마지막번째 값 중의 중간값 선정

### Example
```python
# Quick Sort를 단순 구현
def quick_sort(data, r):
  for rx, ry in r:
    if rx >= ry:
      continue
    pivot = rx

    left, right = rx + 1, ry

    while left <= right:
      while left <= ry and data[left] <= data[pivot]:
        left += 1
      while right > rx and data[right] >= data[pivot]:
        right -= 1

      if left > right:
        data[right], data[pivot] = data[pivot], data[right]
      else:
        data[right], data[left] = data[left], data[right]

    quick_sort(data, [[rx, right - 1], [right + 1, ry]])
quick_sort(data, [[0, len(data) - 1]])
```
```python
# Qucik Sort를 python 장점을 활용하여 간단하게 구현 (연산횟수 증가로 다소 비효율적)
def quick_sort(data):
  if len(data) <= 1:
    return data

  p = data[0]
  tail = data[1:]

  left = [x for x in tail if x <= p]
  right = [x for x in tail if x > p]

  return quick_sort(left) + [p] + quick_sort(right)
```

### 시간 복잡도
#### 평균 복잡도
___O(NlogN)___
#### 최악의 경우
Hoare Partition : Pivot이 왼쪽일 때는 값이 최솟값을 때, Pivot이 오른쪽일 때는 값이 최댓값일 때 분할이 발생 X
Lomuto Partition : 모든 인자가 같거나 이미 정렬된 배열일지라도 swap 발생
___O(N^2)___

### 장점
- 가장 빠른 속도 O(NlogN)
- In-place Sorting

### 단점
- 불균형 분할이라는 특징으로 거의 정렬된 리스트에 대하여 속도 저하 O(N^2)
- Unstable Sort


## Count Sort(계수 정렬)
1. 가장 큰 값과 작은 값의 범위가 모두 담기는 리스트 생성(== 크기가 가장 큰 값과 작은 값의 차인 리스트)
2. 정렬할 리스트 값을 확인하며 (1.)에서 생성한 리스트의 동일한 인덱스의 값 증가

### Example
```python
count = [0] * (max(data) + 1)

for i in range(len(data)):
  count[data[i]] += 1

for i in range(len(count)):
  for k in range(count[i]):
    print(i, end=" ")
```

### 시간 복잡도
값 하나씩 확인하기 하며 인덱스 값 증가 => N
리스트 각 인덱스에 해당하는 값 확인 => 최대값 크기만큼만 => K(최댓값)
___O(N + K)___

### 장점
- 구현이 간단
- 값의 범위가 한정되어 있다면 매우 빠른 속도 O(N + K)
- 최악의 경우에도 O(N + K) 보장
- 리스트 내의 값이 중복될 수록 효과적

### 단점
- 최댓값과 최솟값의 차가 1,000,000을 넘지 않을 때 효율적
- 최댓값과 최솟값의 차가 크면 공간 비효율성 초래 O(N + K) ex) [0, 999999] => 1,000,000 크기의 리스트 선언
