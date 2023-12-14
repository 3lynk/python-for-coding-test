# Sorting(정렬)
데이터를 특정한 기준에 따라서 순서대로 나열하는 것

### Stable Sort
중복된 데이터를 원래 순서와 동일하게 정렬
### Unstable Sort
중복된 데이터가 원래 순서와 다르게 정렬될 가능성 존재

## Selection Sort(선택 정렬)
1. 데이터 중에서 최소값 데이터 탐색
2. 최소값의 데이터가 가장 앞의 데이터 보다 작다면 Swap
3. 가장 앞의 데이터를 제외하고 반복

### Example
```python
for i in range(data):
  min = i

  for k in range(i + 1, len(data)):
    if data[k] < data[min]:
      min = k

  data[k], data[min] = data[min], data[k]
```

### 시간 복잡도
(N - 1) + (N - 2) + ... + 1  
=> N * (N - 1) / 2  

__O(N^2)__

### 장점
- 구현이 간단
- 리스트 안에서 교환하는 방식 => 다른 메모리 사용 X (In-place sorting : 제자리 정렬)
- Bubble Sort에 비해 실제 Swap 횟수 ↓ => Bubble Sort 보다는 조금 더 빠름

### 단점
- 최선의 경우에도 O(N^2) => 비효율적
- Unstable Sort
