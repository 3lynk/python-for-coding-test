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
#### 최악의 경우
1 + 2 + ... + (N - 2) + (N - 1)  
=> N * (N - 1) / 2  
___O(N^2)___

#### 최선의 경우
1 + 1 + ... + 1 + 1  
=> N - 1  
___O(N)___

### 장점
- 구현이 간단
- 데이터가 거의 정렬된 상태라면 매우 빠르게 동작
- 시간 복잡도가 O(N^2)인 Bubble Sort, Selection Sort에 비해 속도 ↑
- Stable Sort
- In-place sorting

### 단점
- 평균과 최악의 경우 O(N^2) => 비효율적

## Quick Sort(퀵 정렬)
1. 
