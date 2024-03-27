# Binary Search(이진 탐색)

## Sequtential Search(순차 탐색)
리스트 안에서 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인 하는 방법

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

## Binary search(이진 탐색)
