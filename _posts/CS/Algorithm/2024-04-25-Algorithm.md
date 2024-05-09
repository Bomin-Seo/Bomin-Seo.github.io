---
layout: single
title:  "Algorithm 분석"
date:   2024-04-25 13:08:52 +0900
categories: Algorithm
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Algorithm
---
## Algorithm
- 문제를 해결할 수 있는 잘 정의된, 유한 시간 내에 종료되는 계산적인 절차
- 입력을 받아 출력으로 전환시켜주는 일련의 계산절차
- 확률적 알고리즘과 같은 무작위성을 포함합니다. 

## 알고리즘의 분석

### Space complexity
- 입력 크기에 따라 메모리가 얼마나 필요할지 결정하는 절차

### Time complexity
- 입력 크기에 따라 단위연산이 몇 번 수행되는지 결정하는 절차
- 알고리즘이 수행되는 하드웨어에 따라 해결하는 시간이 달라집니다.

## 분석 방법

### Every case analysis 
- 입력 크기에만 종속되며 입력 값과는 무관하게 항상 일정한 결과값을 도출합니다.

### Worst case analysis 
- 입력 크기와 입력 값에 종속되며, 단위 연산이 수행되는 수가 최대인 경우를 선택합니다.

### Average Case analysis
- 입력 크기에 종속하며, 모든 입력에 대한 단위 연산이 수행되는 기대값을 선택합니다.
- 각 입력에 대해 확률을 할당할 수 있으며, 일반적으로 worst case 분석보다 복잡한 계산도를 가집니다.

### Best case analysis
- 입력 크기와 입력값 모두에 종속하며, 단위 연산이 수행되는 수가 최소인 경우를 선택합니다.

## 복잡도 함수

### Asymptotic behavior
- 함수나 알고리즘의 입력 크기가 매우 커질 때 어떻게 변화하는지에 대해 설명합니다.
- 함수와 알고리즘에서 높은 차수의 행동과 유사하게 행동함으로써 입력 크기에 따른 성능 변화를 예측할 수 있습니다.

### Big-O O()
#### 정의 : 점근적 상한 (Asymptotic upper bound)
- 복잡도 함수 f(n)에 대해서 g(n) &isin; O(f(n))이면 n &ge; N인 모든 정수 n에 대해서 0 &le; g(n) &le; c * f(n)이 성립하는 양의 실수 c와 음이 아닌 정수 N이 존재한다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/f465a257-e528-4587-8689-b6b9fc978419" height="30%" width = "30%"/></p>

- 함수 g(n)이 $$O(n^2)$$에 속한다
    - n이 커짐에 따라(n이 임의의 값 N보다 큰 값에 대해서) 어떤 2차함수 $$cn^2$$보다 작은 값을 가짐을 뜻합니다.
    - g(n)은 어떤 2차함수 $$cn^2$$보다 빠르다는 것을 의미합니다.

- 알고리즘의 시간 복잡도가 O(f(n))이라면
    - 입력의 크기 n에 대해서 이 알고리즘의 수행 시간은 아무리 늦어도 c*f(n) 이하를 만족함을 의미합니다. (점근적 상한)
    - 이 알고리즘의 수행 시간은 c * f(n)보다 느리지 않음을 의미합니다.

### Omega  $$\Omega()$$
#### 정의 : 점근적 하한 (Asymptotic lower bound)
- 복잡도 함수 f(n)에 대해서 g(n) &isin; O(f(n))이면 n &ge; N인 모든 정수 n에 대해서 g(n) &ge; c * f(n) &ge; 0 이 성립하는 양의 실수 c와 음이 아닌 정수 N이 존재한다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/79be957d-73ce-49db-b313-ee3b0f458cb7" height="30%" width = "30%"/></p>

- 함수 g(n)이 $$\Omega(n^2)$$에 속한다
    - n이 커짐에 따라(n이 임의의 값 N보다 큰 값에 대해서) 어떤 2차함수 $$cn^2$$보다 큰 값을 가짐을 뜻합니다.
    - g(n)은 어떤 2차함수 $$cn^2$$보다 느리다는 것을 의미합니다.

- 알고리즘의 시간 복잡도가 $$\Omega(f(n))$$이라면
    - 입력의 크기 n에 대해서 이 알고리즘의 수행 시간은 아무리 빨라도 c*f(n) 이상임을 의미합니다. (점근적 하한)
    - 이 알고리즘의 수행 시간은 c * f(n)보다 빠를 수 없음을 의미합니다.

### Theta  $$\Theta()$$
#### 정의 : Asymptotic tight bound
- 복잡도 함수 f(n)에 대해서 $$\Theta(f(n)) = O(f(n)) \cap \Omega(f(n)) $$
- n &ge; N인 모든 정수 n에 대해서 c*f(n) &le; g(n) &le; d*f(n) 이 성립하는 양의 실수 c와 d, 음이 아닌 정수 N이 존재한다.
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/d95ff348-0c4c-4620-a61b-2917c0b0c816" height="30%" width = "30%"/></p>

### small-o o()
#### 정의 
- 복잡도 함수간의 관계를 나타내기 위한 표기법
- 복잡도 함수 f(n)에 대해서 g(n) &isin; o(f(n))이면 모든 양의 실수 c에 대하여, n &ge; N인 모든 정수 n에 대해서 0 &le; g(n) &le; c * f(n)이 성립하는 양의 실수 c와 음이 아닌 정수 N이 존재한다.

#### Big-O와의 차이
- Big-O는 양의 실수 c가 하나 이상 성립하면 됩니다.
- small-o는 모든 양의 실수 c에 대해 성립하여야 합니다.