---
layout: single
title:  "[Programmers] 이중 우선 순위 큐"
date:   2024-05-06 13:08:52 +0900
categories: CodingTest
author_profile: true
sidebar:
  nav: "main"
tags : 
    - CodingTest
---
## 문제 
- 이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

|명령어	| 수신 탑(높이)|
|:---:|:---:|
|I 숫자	| 큐에 주어진 숫자를 삽입합니다.|
|D 1| 큐에서 최댓값을 삭제합니다.|
|D -1|  큐에서 최솟값을 삭제합니다.|

- 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

## 조건
- operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
- operations의 원소는 큐가 수행할 연산을 나타냅니다.
    - 원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
- 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

## 풀이 방법
- (Python) heapq를 이용하여 minheap과 maxheap을 구현하고, 문제에서 요구하는 상황에 따라 minheap과 maxheap의 root값을 반환합니다.

## Code
```python
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