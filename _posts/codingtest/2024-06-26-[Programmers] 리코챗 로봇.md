---
layout: single
title:  "[Programmers] 리코쳇 로봇 / 석유 시추"
date:   2024-06-26 13:08:52 +0900
categories: CodingTest
author_profile: true
sidebar:
  nav: "main"
tags : 
    - CodingTest
---

**[Programmers] 리코쳇 로봇**

 <https://school.programmers.co.kr/learn/courses/30/lessons/169199?language=python3>

## 문제 
- 리코쳇 로봇이라는 보드게임이 있습니다.
- 이 보드게임은 격자모양 게임판 위에서 말을 움직이는 게임으로, 시작 위치에서 목표 위치까지 최소 몇 번만에 도달할 수 있는지 말하는 게임입니다.
- 이 게임에서 말의 움직임은 상, 하, 좌, 우 4방향 중 하나를 선택해서 게임판 위의 장애물이나 맨 끝에 부딪힐 때까지 미끄러져 이동하는 것을 한 번의 이동으로 칩니다.
- 다음은 보드게임판을 나타낸 예시입니다.

```
...D..R
.D.G...
....D.D
D....D.
..D....
```

- 여기서 "."은 빈 공간을, "R"은 로봇의 처음 위치를, "D"는 장애물의 위치를, "G"는 목표지점을 나타냅니다.
- 위 예시에서는 "R" 위치에서 아래, 왼쪽, 위, 왼쪽, 아래, 오른쪽, 위 순서로 움직이면 7번 만에 "G" 위치에 멈춰 설 수 있으며, 이것이 최소 움직임 중 하나입니다.
- 게임판의 상태를 나타내는 문자열 배열 board가 주어졌을 때, 말이 목표위치에 도달하는데 최소 몇 번 이동해야 하는지 return 하는 solution함수를 완성하세요. 만약 목표위치에 도달할 수 없다면 -1을 return 해주세요.

## 조건
- 3 ≤ board의 길이 ≤ 100
    - 3 ≤ board의 원소의 길이 ≤ 100
    - board의 원소의 길이는 모두 동일합니다.
    - 문자열은 ".", "D", "R", "G"로만 구성되어 있으며 각각 빈 공간, 장애물, 로봇의 처음 위치, 목표 지점을 나타냅니다.
    - "R"과 "G"는 한 번씩 등장합니다.

## 풀이 방법
- 현재의 위치와 이동횟수를 queue에 저장하고, 가장 먼저 저장된 (위치, 이동횟수)를 기반으로 경우의 수를 탐색합니다.
- 현재의 위치에서 동/서/남/북으로 이동이 가능한 경우 해당 방향으로 최대한 이동합니다.
- 변화된 위치가 골인지점과 일치한다면 위치를 반환하며, 일치하지 않다면 현재의 (위치, 이동횟수)를 queue에 저장합니다.
- 방문한 위치를 저장하여 같은 곳을 재방문하게 된다면 -1을 반환합니다.

## Code
```python
from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    start, goal = False, False

    for i in range(n):
        for j in range(m):
            if board[i][j] == "R" :
                start = (i, j)
            elif board[i][j] == "G":
                goal = (i, j)

        if start and goal: break

    direc = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque([(start[0], start[1], 0)])
    visited = {start}

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == goal: return cnt
        
        for dx, dy in direc:
            nx, ny = x, y

            while 0<= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != "D":
                nx += dx
                ny += dy
            
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, cnt + 1))
    return -1
```

-----------------------------------------------------------------------------------------------------------------------

**[Programmers] [PCCP 기출문제] 2번 / 석유 시추**

 <https://school.programmers.co.kr/learn/courses/30/lessons/250136>


## 문제 

- 세로길이가 n 가로길이가 m인 격자 모양의 땅 속에서 석유가 발견되었습니다. 석유는 여러 덩어리로 나누어 묻혀있습니다. 
- 당신이 시추관을 수직으로 단 하나만 뚫을 수 있을 때, 가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾으려고 합니다. 
- 시추관은 열 하나를 관통하는 형태여야 하며, 열과 열 사이에 시추관을 뚫을 수 없습니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/674f7761-585f-4d50-9016-d9250f419ed2" height="70%" width = "70%"/></p>

- 예를 들어 가로가 8, 세로가 5인 격자 모양의 땅 속에 위 그림처럼 석유가 발견되었다고 가정하겠습니다. 
- 상, 하, 좌, 우로 연결된 석유는 하나의 덩어리이며, 석유 덩어리의 크기는 덩어리에 포함된 칸의 수입니다. 그림에서 석유 덩어리의 크기는 왼쪽부터 8, 7, 2입니다.

<p align='center'><img src = "https://github.com/Bomin-Seo/project1/assets/94039896/77c5ac2b-7d56-4991-b6e4-58aa86be2c14" height="70%" width = "70%"/></p>

- 시추관은 위 그림처럼 설치한 위치 아래로 끝까지 뻗어나갑니다. 
- 만약 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다. 
- 시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다. 
- 시추관을 설치한 위치에 따라 뽑을 수 있는 석유량은 다음과 같습니다.

|시추관의 위치|획득한 덩어리| 총 석유량|
|:---:|:---:|:---:|
|1|	[8]|	8|
|2	|[8]	|8|
|3	|[8]	|8|
|4	|[7]	|7|
|5	|[7]	|7|
|6	|[7]	|7|
|7	|[7, 2]|	9|
|8	|[2]	|2|

- 오른쪽 그림처럼 7번 열에 시추관을 설치하면 크기가 7, 2인 덩어리의 석유를 얻어 뽑을 수 있는 석유량이 9로 가장 많습니다.
- 석유가 묻힌 땅과 석유 덩어리를 나타내는 2차원 정수 배열 land가 매개변수로 주어집니다. 
- 이때 시추관 하나를 설치해 뽑을 수 있는 가장 많은 석유량을 return 하도록 solution 함수를 완성해 주세요.

## 조건

- 1 ≤ land의 길이 = 땅의 세로길이 = n ≤ 500
    - 1 ≤ land[i]의 길이 = 땅의 가로길이 = m ≤ 500
    - land[i][j]는 i+1행 j+1열 땅의 정보를 나타냅니다.
    - land[i][j]는 0 또는 1입니다.
    - land[i][j]가 0이면 빈 땅을, 1이면 석유가 있는 땅을 의미합니다.

##### 정확성 테스트 케이스 제한사항
- 1 ≤ land의 길이 = 땅의 세로길이 = n ≤ 100
    - 1 ≤ land[i]의 길이 = 땅의 가로길이 = m ≤ 100

## 풀이 방법
- 효율성 테스트 통과를 위해 DFS보다 Queue를 이용한 BFS를 이용합니다.
- 모든 요소를 순회하며, 방문하지 않았으며 해당 칸의 석유양이 1인 경우 search함수를 이용하여 석유 덩어리의 전체 양을 계산합니다.
- BFS를 이용하여 연결된 칸의 전체 석유양과 해당 석유가 존재하는 열의 index를 집합 cols에 담아 반환합니다.
- 집합 cols에 담긴 열의 index를 키로 가지는 default dict의 value에 전체 석유 덩어리의 양을 합합니다.

## Code

```python
from collections import defaultdict, deque

def search(n, m, x, y, land, visited, tot, c):
    direc = [(1, 0), (-1, 0), {0, 1}, (0, -1)]
    q, tot = deque([(x, y)]), 1
    cols = {y}
    while q:
        cx, cy = q.popleft()
        for dx, dy in  direc:
            nx, ny = cx + dx, cy + dy
            if  0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                tot += 1
                cols.add(ny)
    return tot, cols

def solution(land):
    n, m = len(land), len(land[0])
    visited = [([False] * m) for _ in range(n)]
    dict_ = defaultdict(int)

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                visited[i][j] = True
                tot, cols = search(n, m, i, j, land, visited, 1, [j])
                for col in cols:
                    dict_[col] += tot
    
    return dict_[max(dict_, key=dict_.get)]
```