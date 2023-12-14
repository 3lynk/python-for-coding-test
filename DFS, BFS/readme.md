# Data Structure(자료구조)
데이터를 표현하고 관리하고 처리하기 위한 구조 ___ex) Stack, Queue___  
  
Push : 데이터 삽입  
Pop : 데이터 삭제  
Overflow : 수용할 수 있는 데이터 저장공간이 가득 찬 상태에서 Push 할 때 발생  
Underflow : 데이터가 전혀 없는 상태에서 Pop 할 때 발생

## Stack(스택)
First In Last Out, Last In First Out  
```python
stack = []

stack.append(value1)
stack.append(value2)
stack.append(value3)
stack.pop()

print(stack)

# Output : [value1, value2]
```

## Queue(큐)
First In First Out  
collection 모듈의 deque 활용  
deque가 queue 라이브러리 보다 간단  
deque 객체로 반환하기 때문에 list() 메서드로 list로 반환 가능
```python
from collections import deque

queue = deque()

queue.append(value1)
queue.append(value2)
queue.append(value3)
queue.popleft()

print(queue)

# Output : deque([value2, value3])
```

## Recursive Function(재귀 함수)
자기 자신을 다시 호출  
종료 조건을 꼭 명시해야 함


# Search(탐색)
많은 양의 데이터 중에서 원하는 데이터를 찾는 과정 _ex) DFS, BFS_  

__그래프 표현 방식__
- Adjacency Matrix(인접 행렬)
  - 2차원 배열로 그래프의 연결 관계를 표현
  - 각 노드와 모든 노드의 관계 정보를 저장
  - 직접적으로 연결 되어 있지 않은 정보는 Infinity 비용(주로 999999999, 987654321 등의 값으로 초기화)
  - [a, b] -> a와 b의 연결된 정보
  - __모든 관계 저장 -> 노드 개수가 많을 수록 메모리 낭비__
  - _ex) [[0, 3, 5, 999999999], [3, 0, 999999999, 999999999], [5, 999999999, 0, 7], [99999999, 999999999, 7, 0]]_
- Adjacency List(인접 리스트)
  - 리스트로 그래프의 연결 관계를 표현
  - 각 노드에 연결되어 있는 노드와 관계 정보를 저장
  - [n] -> n관 연결된 노드들의 정보
  - __연결된 정보만 저장 -> 메모리 효율적, 특정 두 노드가 연결되어 있는지 확인이 어려움__
  - __특정 노드와 연결된 모든 인접 노드 순회시 메모리 효율적__
  - _ex) [[(1, 3), (2, 5)], [(0, 3)], [(0, 5), (3, 7)], [(2, 7)]]_

## DFS(깊이 우선 탐색)
Depth-First Search  
  
__동작 과정__
1. 탐색 시작 노드를 스택에 삽입, 방문 처리
2. 스택 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리 / 방문하지 않은 인접 노드가 없으면 최상단 노드 꺼내기
3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복
  
__특징__
- 스택 자료구조에 기초 -> 구현이 간단
- 실제로는 스택 사용 안해도 됨
- 시간 복잡도 : O(N) (데이터 개수 : N)

```python
def dfs(graph, v, visited):
  visited[v] = True

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)
```

## BFS(너비 우선 탐색)
Breadth First Search  

__동작 과정__  
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 및 방문 처리
3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복

__특징__  
- 큐 자료구조에 기초 -> 구현이 간단
- deque 라이브러리 사용하면 편리
- 시간 복잡도 : O(N) (데이터 개수 : N)
- DFS 속도 < BFS 속도 (일반적인 경우)

```python
import colletions import deque

def bfs(graph, start, visited):
  queue = deque([start])

  visited[start] = True

  while queue:
    v = queue.popleft()

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
```
