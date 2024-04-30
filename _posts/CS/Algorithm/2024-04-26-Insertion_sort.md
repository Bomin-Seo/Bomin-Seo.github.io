---
layout: single
title:  "Algorithm - Sorting : Insertion Sort"
date:   2024-04-26 13:08:52 +0900
categories: Algorithm Sorting
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Algorithm
    - Sorting
---
## Insertion Sort
- $$O(n^2)$$ 정렬 알고리즘
- 정렬 범위를 1에서부터 점차적으로 1씩 늘려가며 정렬하는 알고리즘
- 새로 정렬 범위에 들어온 항목을 이미 정렬되어 있는 배열의 항목과 비교 및 교체를 수행하여 적절한 위치에 끼워넣는 정렬 알고리즘
- 일정 수준 정렬된 데이터에 대해 빠르게 수행되는 알고리즘
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/1d59636f-ab30-4aff-9af5-7514bc79cc90" height="40%" width = "40%"/></p>

### 공간 복잡도 분석
- in-place sorting algorithm으로 추가적인 저장 장소가 필요하지 않다.
- 따라서, $$M(n) = \Theta(1)$$

### 시간 복잡도 분석

#### Case별 시간복잡도
- Best Case : $$O(n)$$  /   Average Case : $$O(n^2)$$   /   Worst Case : $$O(n^2)$$

#### Worst Case
- 역순으로 정렬되어 있는 경우
- ex) 5 4 3 2 1 &rarr; 4 5 3 2 1 &rarr; 3 4 5 2 1 &rarr; 2 3 4 5 1 &rarr; 1 2 3 4 5
- 현재의 정렬 범위가 i일 때, 정렬을 수행하는 반복문 안에서 최대 i-1번의 비교가 이루어진다.
- 역순으로 정렬된 경우 n개의 항목에 대해 총 비교 연산의 회수는 $$W(n) = \sum(i-1) = \frac{n(n-1)}{2} \approx \frac{n^2}{2}$$

#### Average Case
- 현재의 정렬 범위가 i인 경우, 새로 정렬 범위에 추가된 항목 x가 위치할 수 있는 위치는 i개가 존재한다.
- x가 특정 위치에 위치하기 위해 수행되는 비교 연산의 횟수는

| index | 1 | 2 | 3 | ... | i-1 | i | 
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 비교연산 | i-1 | i-1 | i - 2 | ... | 2 | 1|

  이며 x가 1번 혹은 2번 index의 데이터가 될 경우 비교 연산의 횟수는 i-1번으로 동일하다.

- x가 각 위치의 데이터가 될 확률은 $$\frac{1}{i}$$이다.
- x를 삽입하기 위해 필요한 평균 비교 회수는 $$(\frac{1}{i})\times (1 + 2 + ... + i-1 + i-1) = \frac{1}{i} \times \sum k + \frac{i-1}{i} = \frac{i+1}{2} - \frac{1}{i}$$
- n개의 항목을 정렬하는데 수행되는 비교 회수는 $$\sum (\frac{i+1}{2} - \frac{1}{i}) = \sum \frac{i+1}{2} - \sum \frac{1}{i} \approx \frac{(n+4)(n-1)}{4} - \ln(n) \approx \frac{n^2}{4}$$

### python code 1
```
def insertion_sort(values):
    numvalues, count = len(values), 0
    while count < numvalues:
        finished = False
        current = count
        moretosearch = current != 0
        while moretosearch and not finished:
            if values[current] < values[current - 1]:
                values[current], values[current - 1] = values[current - 1], values[current]
                current -= 1
                moretosearch = current != 0
            else:
                finished = True
        count += 1
```

### python code 2
```
def insertion_sort(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
```

### java code
```
public class Insertion {
    public static void sort(int[] arr) {
        for (int end = 1; end < arr.length; end++) {
            int i = end;
            while (i > 0 && arr[i - 1] > arr[i]) {
                swap(arr, i - 1, i);
                i--;
            }
        }
    }
    private static void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
}
```