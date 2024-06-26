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

## Tree(트리 자료구조)
노드와 노드의 연결로 표현하는 그래프 자료구조의 일종

### 용어
- Root Node(루트 노드) : 트리의 최상단 노드, 부모가 없는 노드
- Leaf Node(단말 노드) : 자식이 없는 노드
- Edge(간선, Link, Branch) : 노드를 연결하는 선
- Sibling(형제) : 같은 부모를 가진 노드
- Size(크기) : 자신을 포함한 모든 자손 노드의 개수
- Depth(깊이) : Root Node에서 특정 노드에 도달하기까지의 Edge 개수
- Level(레벨) : 특정 Depth를 가지는 노드 집합
- Degree(차수) : 자식 트리의 개수
- Degree of Tree(트리의 차수) : 트리의 최대 차수
- Height(트리의 높이) : Maximum Depth
- Sub Tree(서브 트리) : 트리에서 일부를 때어낸 트리


### 특징
- 데이터베이스 시스템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를 관리하기 위해 사용
- 트리의 일부를 때어내도 트리 구조
- 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합
- 이진 탐색과 같은 탐색 기법으로 빠르게 탐색 가능
- 부모 노드와 자식 노드의 관계로 표현
- 노드가 N개인 트리는 (N - 1)개의 Edge 소유
- 임의의 두 노드간의 경로는 유일
