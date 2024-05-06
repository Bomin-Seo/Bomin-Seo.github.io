---
layout: single
title:  "[Python] Heapq"
date:   2024-05-06 13:08:52 +0900
categories: DataStructure
author_profile: true
sidebar:
  nav: "main"
tags : 
    - DataStructure
---
## Data Structure - heapq
- 이 모듈은 우선순위 큐, heap 큐 알고리즘 구현을 제공합니다.
- 0번 index부터 indexing을 사용하며 minheap 구현을 제공합니다.
- 포함된 method는 연산 중 heap 불변성을 유지하며, 값이 들어있는 데이터는 heapify()를 통해 heap으로 변환합니다.

### Method
- heapq.heapify(x)
    - 이미 값을 가지고 있는 리스트 x를 선형 시간으로 제자리에서 힙으로 변환합니다.

```
heap = [3 ,1, 2]
heapq.heapify(heap) # [1, 3, 2]
```

- heapq.heapush(heap, item)
    - heap 불변성을 유지하면서, item을 heap으로 push합니다.

```
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# heap = [1, 3, 2]
```

- heapq.heappop(heap, item)
    - heap 불변성을 유지하면서, heap에서 가장 작은 항목을 pop한 후 반홥합니다.
    - heap이 비어있는 경우 IndexError가 발생합니다.
    - heap의 변경시키지 않고 가장 작은 데이터에 접근하는 경우 heap[0]을 사용합니다.

```
result = heapq.heappop(heap)

# result : 1    /   heap = [2, 3]
```

- heapq.heappushpop(heap, item)
    - heap에 item을 push 한 다음 heap에서 가장 작은 항목을 pop하고 반환합니다.
    - heappush() 실행 후 heappop()을 호출하는 경우보다 더 효율적으로 실행됩니다.

- heapq.heapreplace(heap, item)
    - heap에서 가장 작은 항목을 pop하고 반환한 후 새로운 item을 push합니다.
    - heap이 비어있는 경우 IndexError가 발생합니다.
    - heappop() 실행 후 heappush()하는 것보다 효율적으로 실행됩니다.
    - heap의 크기가 변하지 않기 때문에 고정 크기 heap을 사용할 때 적합합니다.

- heapq.merge(*iterables, key=None, reverse=False)
    - 여러 개의 정렬된 sequence를 단일 병합된 sequence로 반환합니다.
    - key와 reverse는 sorted()와 같이 정렬기준과 역순정렬의 여부를 입력합니다.

```
import heapq

list1 = [(1, 'apple'), (3, 'banana'), (2, 'orange')]
list2 = [(4, 'grape'), (6, 'melon'), (5, 'strawberry')]

# 각 튜플의 첫 번째 요소를 기준으로 정렬
merged_list = heapq.merge(list1, list2, key=lambda x: x[0])

# 정렬된 시퀀스(iterable)를 리스트로 변환하여 출력
print(list(merged_list))
```

- heapq.nlargest(n, iterable, key=None)
    -  iterable에 의해 정의된 데이터 집합에서 n개의 가장 큰 요소로 구성된 리스트를 반환합니다.

- heapq.nsmallest(n, iterable, key=None)
    - iterable에 의해 정의된 데이터 집합에서 n 개의 가장 작은 요소로 구성된 리스트를 반환합니다.

### Maxheap
- 데이터에 -1을 곱한 후 heappush()를 수행합니다.
- 데이터를 반환받는 과정에서 다시 -1을 곱하여 값을 반환받습니다.

```
heapq.heappush(maxheap, -int(num))
```

### 예제
- [Programmers] 이중 우선순위 큐 : [문제보기](https://bomin-seo.github.io/codingtest/Programmers-%EC%9D%B4%EC%A4%91%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%ED%81%90/)

```
import heapq

def solution(operations):
    minheap = []
    maxheap = []
    for i in operations:
        operation, num = i.split(" ")
        if operation == 'I':
            heapq.heappush(minheap, int(num))
            heapq.heappush(maxheap, -int(num))
        else:
            if not minheap:
                continue
            elif num == '1':
                heapq.heappop(maxheap)
                minheap = [-i for i in maxheap]
                heapq.heapify(minheap)
            else:
                heapq.heappop(minheap)
                maxheap = [-i for i in minheap]
                heapq.heapify(maxheap)
    if not minheap:
        return [0,0]
    else:
        return [-maxheap[0],minheap[0]]
```