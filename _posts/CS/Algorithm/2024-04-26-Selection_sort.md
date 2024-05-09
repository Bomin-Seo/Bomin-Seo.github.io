---
layout: single
title:  "Algorithm - Sorting : Selection Sort"
date:   2024-04-26 13:08:52 +0900
categories: Algorithm Sorting
author_profile: true
sidebar:
  nav: "main"
tags : 
    - Algorithm
    - Sorting
---
## Selection Sort
- 정렬되지 않은 부분에서 가장 작은 값을 앞에 배치하며 정렬하는 알고리즘
- 정렬할 위치가 정해진 상태에서 어떤 요소를 넣을지 선택하는 알고리즘
<p align='center'><img src = "https://github.com/Bomin-Seo/Study/assets/94039896/a91e9655-8f3b-41d8-9b9d-4f66645cae8e" height="30%" width = "30%"/></p>
- 데이터의 정렬 여부에 관계 없이 동일한 비교 연산을 수행하기에 타 정렬 알고리즘에 비해 성능이 떨어집니다.
- 같은 키값을 가지는 데이터 간의 정렬 전 순서가 보장되지 않는 unstable 정렬 방법

### 공간 복잡도 분석
- in-place sorting algorithm으로 추가적인 저장 장소가 필요하지 않습니다.
- 따라서, $$M(n) = O(1)$$

### 시간 복잡도 분석

#### Case별 시간복잡도
- Best Case : $$O(n^2)$$  /   Average Case : $$O(n^2)$$   /   Worst Case : $$O(n^2)$$
- 정렬 여부에 상관없이 동일 비교 연산 수행

#### Every Case
- 정렬이 진행될수록 최소값을 찾아내는 비교 연산 수행 횟수가 줄어듭니다. 
- n개의 항목에 대해서 비교 연산 횟수는 n-1, n-2, ..., 2, 1이 됩니다.
- $$T(n) = \frac{n(n-1)}{2}$$

### python code 
```
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

### java code
```
public class Selection {
    public static void sort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIdx])
                    minIdx = j;
            }
            swap(arr, i, minIdx);
        }
    }
    private static void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
}
```