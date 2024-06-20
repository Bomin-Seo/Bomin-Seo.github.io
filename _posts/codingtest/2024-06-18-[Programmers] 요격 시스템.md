---
layout: single
title:  "[Programmers] 요격 시스템 / 광물 캐기"
date:   2024-06-18 13:08:52 +0900
categories: CodingTest
author_profile: true
sidebar:
  nav: "main"
tags : 
    - CodingTest
---

**[Programmers] 요격 시스템**

 <https://school.programmers.co.kr/learn/courses/30/lessons/181188>

## 문제 
- A 나라가 B 나라를 침공하였습니다. B 나라의 대부분의 전략 자원은 아이기스 군사 기지에 집중되어 있기 때문에 A 나라는 B 나라의 아이기스 군사 기지에 융단폭격을 가했습니다. A 나라의 공격에 대항하여 아이기스 군사 기지에서는 무수히 쏟아지는 폭격 미사일들을 요격하려고 합니다. 이곳에는 백발백중을 자랑하는 요격 시스템이 있지만 운용 비용이 상당하기 때문에 미사일을 최소로 사용해서 모든 폭격 미사일을 요격하려 합니다. 
- A 나라와 B 나라가 싸우고 있는 이 세계는 2 차원 공간으로 이루어져 있습니다. A 나라가 발사한 폭격 미사일은 x 축에 평행한 직선 형태의 모양이며 개구간을 나타내는 정수 쌍 (s, e) 형태로 표현됩니다. 
- B 나라는 특정 x 좌표에서 y 축에 수평이 되도록 미사일을 발사하며, 발사된 미사일은 해당 x 좌표에 걸쳐있는 모든 폭격 미사일을 관통하여 한 번에 요격할 수 있습니다. 
- 단, 개구간 (s, e)로 표현되는 폭격 미사일은 s와 e에서 발사하는 요격 미사일로는 요격할 수 없습니다. 요격 미사일은 실수인 x 좌표에서도 발사할 수 있습니다.
- 각 폭격 미사일의 x 좌표 범위 목록 targets이 매개변수로 주어질 때, 모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟값을 return 하도록 solution 함수를 완성해 주세요.

## 조건
- 1 ≤ targets의 길이 ≤ 500,000
    - targets의 각 행은 [s,e] 형태입니다.
    - 이는 한 폭격 미사일의 x 좌표 범위를 나타내며, 개구간 (s, e)에서 요격해야 합니다.
- 0 ≤ s < e ≤ 100,000,000

## 풀이 방법
- 폭격 미사일의 범위 (s, e)에서 e를 기준으로 오름차순으로 정렬합니다.
- 반복을 거쳐 check point(cp)값을 0에서부터 개구간의 끝값 e값들로 순차적으로 증가시킵니다.
- 이전의 cp와 현재의 cp사이에서 개구간의 시작 값 s가 포함된다면 answer을 1 증가시킵니다. 

## Code
```python
def solution(targets):
    answer = 0
    targets = sorted(targets, key = lambda x :(x[1], x[0]))
    cp = 0
    for i in targets:
        if i[0] >= cp:
            answer += 1
            cp = i[1]
    return answer
```

-----------------------------------------------------------------------------------------------------------------------

**[Programmers] 요격 시스템**

 <https://school.programmers.co.kr/learn/courses/30/lessons/172927>


## 문제 
- 마인은 곡괭이로 광산에서 광석을 캐려고 합니다. 마인은 다이아몬드 곡괭이, 철 곡괭이, 돌 곡괭이를 각각 0개에서 5개까지 가지고 있으며, 곡괭이로 광물을 캘 때는 피로도가 소모됩니다. 각 곡괭이로 광물을 캘 때의 피로도는 아래 표와 같습니다.

<p align='center'><img src = "https://github.com/kwj0605/outsourcing/assets/94039896/4e3d4611-87c3-49f9-99a8-11e6e2cace9a" height="60%" width = "60%"/></p>

- 예를 들어, 철 곡괭이는 다이아몬드를 캘 때 피로도 5가 소모되며, 철과 돌을 캘때는 피로도가 1씩 소모됩니다. 각 곡괭이는 종류에 상관없이 광물 5개를 캔 후에는 더 이상 사용할 수 없습니다.

- 마인은 다음과 같은 규칙을 지키면서 최소한의 피로도로 광물을 캐려고 합니다.
    - 사용할 수 있는 곡괭이중 아무거나 하나를 선택해 광물을 캡니다.
    - 한 번 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용합니다.
    - 광물은 주어진 순서대로만 캘 수 있습니다.
    - 광산에 있는 모든 광물을 캐거나, 더 사용할 곡괭이가 없을 때까지 광물을 캡니다.
- 즉, 곡괭이를 하나 선택해서 광물 5개를 연속으로 캐고, 다음 곡괭이를 선택해서 광물 5개를 연속으로 캐는 과정을 반복하며, 더 사용할 곡괭이가 없거나 광산에 있는 모든 광물을 캘 때까지 과정을 반복하면 됩니다.

- 마인이 갖고 있는 곡괭이의 개수를 나타내는 정수 배열 picks와 광물들의 순서를 나타내는 문자열 배열 minerals가 매개변수로 주어질 때, 마인이 작업을 끝내기까지 필요한 최소한의 피로도를 return 하는 solution 함수를 완성해주세요.

## 조건
- picks는 [dia, iron, stone]과 같은 구조로 이루어져 있습니다.
    - 0 ≤ dia, iron, stone ≤ 5
    - dia는 다이아몬드 곡괭이의 수를 의미합니다.
    - iron은 철 곡괭이의 수를 의미합니다.
    - stone은 돌 곡괭이의 수를 의미합니다.
    - 곡괭이는 최소 1개 이상 가지고 있습니다.
- 5 ≤ minerals의 길이 ≤ 50
    - minerals는 다음 3개의 문자열로 이루어져 있으며 각각의 의미는 다음과 같습니다.
    - diamond : 다이아몬드  /   iron : 철   /   stone : 돌

## Code

```python
def solution(picks, minerals):
    answer = 0
    if len(minerals) > sum(picks) * 5:
        minerals = minerals[:sum(picks)*5]
    count = []
    for i in range(len(minerals) // 5):
        parts = minerals[i*5:i*5+5]
        count.append([parts.count('diamond'), parts.count('iron'), parts.count('stone')])
    parts = minerals[(len(minerals) // 5) * 5 :]
    count.append([parts.count('diamond'), parts.count('iron'), parts.count('stone')])
    count = sorted(count, key=lambda x:(-x[0], -x[1]))
    while count:
        temp = count.pop(0)
        if picks[0]:
            answer += sum(temp)
            picks[0] -= 1
        elif picks[1]:
            answer += temp[0] *5 + temp[1] + temp[2]
            picks[1] -= 1
        else:
            answer += temp[0] * 25 + temp[1] * 5 + temp[2]
            picks[2] -= 1
            
    return answer
```