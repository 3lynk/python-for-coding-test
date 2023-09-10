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
많은 양의 데이터 중에서 원하는 데이터를 찾는 과정 ___ex) DFS, BFS___

## DFS(깊이 우선 탐색)
Depth-First Search
